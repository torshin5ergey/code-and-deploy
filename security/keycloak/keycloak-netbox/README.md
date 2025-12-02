# NetBox Community + Keycloak Setup OIDC

Tested on NetBox Community 4.2.6, Keycloak 26.3

**Table of Contents:**
- [References](#references)
- [NetBox Setup](#netbox-setup)
- [Keycloak Setup](#keycloak-setup)
  - [Client](#client)
  - [Client Scope Mappers](#client-scope-mappers)

## References

- [Authentication & Permissions | NetBox Documentation](https://netboxlabs.com/docs/netbox/features/authentication-permissions/)
- [Authentication | NetBox Documentation](https://netboxlabs.com/docs/netbox/administration/authentication/overview/)
- [python-social-auth/social-core/social-core/backends/keycloak.py | GitHub](https://github.com/python-social-auth/social-core/blob/master/social_core/backends/keycloak.py)
- [Keycloak - Open Source Red Hat SSO - Python Social Auth](https://python-social-auth.readthedocs.io/en/latest/backends/keycloak.html)
- [Multiple remote auth backends #9479 | GitHub Discussions](https://github.com/netbox-community/netbox/discussions/9479)
- [using openidconnectauth (oidc) #17549 | GitHub Discussions](https://github.com/netbox-community/netbox/discussions/17549)
- [Custom Pipeline for Azure SSO Groups #13129 | GitHub Discussions](https://github.com/netbox-community/netbox/discussions/13129#discussioncomment-9432117)

## NetBox Setup

- [`configuration.py`](/security/keycloak/keycloak-netbox/configuration.py)
```py
# netbox/netbox/netbox/configuration.py

### Keycloak OIDC
REMOTE_AUTH_BACKEND = 'social_core.backends.keycloak.KeycloakOAuth2'
# or use a python list for multiple auth methods
# example: keycloak, ldap
# REMOTE_AUTH_BACKEND = [
#         'social_core.backends.keycloak.KeycloakOAuth2',
#         'netbox.authentication.LDAPBackend'
# ]

SOCIAL_AUTH_KEYCLOAK_KEY = 'netbox'
SOCIAL_AUTH_KEYCLOAK_SECRET = '<KEYCLOAK_CLIENT_SECRET>'
SOCIAL_AUTH_KEYCLOAK_PUBLIC_KEY = '<KEYCLOAK_REALM_PUBLIC_KEY>' # Keycloak > Realm settings > Keys > RS256 Public key
SOCIAL_AUTH_KEYCLOAK_AUTHORIZATION_URL = 'https://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM>/protocol/openid-connect/auth'
SOCIAL_AUTH_KEYCLOAK_ACCESS_TOKEN_URL = 'https://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM>/protocol/openid-connect/token'
SOCIAL_AUTH_BACKEND_ATTRS = {
    'keycloak': ("Login with Keycloak", "login"),
} # button text

# add custom Kyeycloak groups sync pipeline
# netbox.custom_pipeline.set_role
SOCIAL_AUTH_PIPELINE = [
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'netbox.authentication.user_default_groups_handler',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'netbox.custom_pipeline.set_role'
]
### Keycloak OIDC end
```
- [`custom_pipeline.py`](/security/keycloak/keycloak-netbox/custom_pipeline.py)
```py
# netbox/netbox/netbox/custom_pipeline.py
# Sync groups from Keycloak

from django.contrib.auth.models import Group

class AuthFailed(Exception):
    """Custom Auth Exception"""
    pass

def set_role(response, user, backend, *args, **kwargs):
    """
    Get roles from JWT
    Assign user to netbox group matching role
    Also set is_superuser or is_staff for special roles 'superusers' and 'staff'
    """
    try:
        # get roles from 'roles' JWT field
        roles = response['roles']
    except KeyError:
        # if no 'roles' field in JWT
        # clear user groups
        user.groups.clear()
        raise AuthFailed("No role assigned")

    try:
        # reset privileges
        user.is_superuser = False
        user.is_staff = False

        # set privileges
        for role in roles:
            # netbox superuser
            if role == 'netbox_admins':
                user.is_superuser = True
                user.save()
                continue
            # netbox staff
            if role == "netbox_users":
                user.is_staff = True
                user.save()
                continue

            # add to existed groups, uncomment if needed
            #group, created = Group.objects.get_or_create(name=role)
            #group.user_set.add(user)
    except Group.DoesNotExist:
        pass
```

## Keycloak Setup

Don't forget to map Keycloak groups and Client Scopes to corresponding Client Roles

### Client

- Client ID: `netbox`
- Valid redirect URIs: `https://<NETBOX_HOSTNAME>/*`
- Root URL: `https://<NETBOX_HOSTNAME>`
- Home URL: `https://<NETBOX_HOSTNAME>`
- Web Origins: `https://<NETBOX_HOSTNAME>`
- Admin URL: `https://<NETBOX_HOSTNAME>`
- Client authentication: `On`
- Authorizations: `Off`
- Authentication flow: `Standard flow`, `Direct access grants`
- Client Roles:
  - `netbox_admins`
  - `netbox_users`
- Advanced:
  - User info signed response algorithm: `RS256`
  - Request object signature algorithm: `RS256`

### Client Scope Mappers

**Grafana**
  - `aud`: Audience
  - `email`: User Attribute
  - `given_name`: User Attribute (firstName)
  - `preferred_username`: User Attribute (username)
  - `family_name`: User Attribute (lastName)
  - `roles`: User Client Role
  - Scope: `netbox_admins`, `netbox_users`
