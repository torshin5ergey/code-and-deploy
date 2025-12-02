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
