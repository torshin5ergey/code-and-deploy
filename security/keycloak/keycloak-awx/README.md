# AWX+Keycloak Setup SAML

Tested on AWX 17.1.0, Keycloak 26.3

## References

- https://ansible.readthedocs.io/projects/awx/en/24.6.1/administration/ent_auth.html
- https://github.com/ansible/awx/issues/12238

## AWX Setup

- Go to `https://<AWX_HOSTNAME>/api/v2/settings/saml/`
- Update settings
```json
{
  "SAML_AUTO_CREATE_OBJECTS": false,
  "SOCIAL_AUTH_SAML_CALLBACK_URL": "https://<AWX_HOSTNAME>/sso/complete/saml/",
    "SOCIAL_AUTH_SAML_METADATA_URL": "https://<AWX_HOSTNAME>/sso/metadata/saml/",
    "SOCIAL_AUTH_SAML_SP_ENTITY_ID": "https://<AWX_HOSTNAME>", # can be found in `/api/v2/settings/system`, under the `TOWER_URL_BASE` variable
    "SOCIAL_AUTH_SAML_SP_PUBLIC_CERT": "-----BEGIN CERTIFICATE-----certdata-----END CERTIFICATE-----",
    "SOCIAL_AUTH_SAML_SP_PRIVATE_KEY": "-----BEGIN PRIVATE KEY--keydata-----END PRIVATE KEY——",
    "SOCIAL_AUTH_SAML_ORG_INFO": {
        "en-US": {
            "displayname": "Keycloak",
            "url": "https://<KEYCLOAK_HOSTNAME>",
            "name": "Keycloak"
        }
    },
    "SOCIAL_AUTH_SAML_TECHNICAL_CONTACT": {
        "emailAddress": "admin@company.com",
        "givenName": "Admin User"
    },
    "SOCIAL_AUTH_SAML_SUPPORT_CONTACT": {
        "emailAddress": "support@company.com",
        "givenName": "Support Team"
    },
    "SOCIAL_AUTH_SAML_ENABLED_IDPS": {
        "Keycloak": {
            "url": "https://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM>/protocol/saml",
            "attr_user_permanent_id": "user_name",
            "attr_last_name": "last_name",
            "attr_first_name": "first_name",
            "attr_email": "email",
            "x509cert": "certdata", # https://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM>/protocol/saml/descriptor under `ds:X509Certificate`
            "attr_username": "user_name",
            "entity_id": "https://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM>",
            "attr_groups": "is_org_admin"
        }
    },
    "SOCIAL_AUTH_SAML_SECURITY_CONFIG": {
        "requestedAuthnContext": false
    },
    "SOCIAL_AUTH_SAML_SP_EXTRA": null,
    "SOCIAL_AUTH_SAML_EXTRA_DATA": null,
    "SOCIAL_AUTH_SAML_ORGANIZATION_MAP": {},
    "SOCIAL_AUTH_SAML_TEAM_MAP": null,
    "SOCIAL_AUTH_SAML_ORGANIZATION_ATTR": {
        "saml_admin_attr": "is_org_admin",
        "saml_attr": "is_org_admin",
        "remove": true,
        "remove_admins": true
    },
    "SOCIAL_AUTH_SAML_TEAM_ATTR": {}
}
```

## Keycloak Setup

Don't forget to map Keycloak groups and Client Scopes to corresponding Client Roles

### Client

- Client ID: `<AWX_HOSTNAME>` (`TOWER_URL_BASE`)
- Valid redirect URIs: `https://<AWX_HOSTNAME>/sso/complete/saml/`
- Master SAML Processing URL: `https://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM>/protocol/saml/`
- Name ID format: `username`
- Sign documents: `On`
- Sign assertions: `On`
- Client Roles:
  - `awx_administrators`
  - `awx_users`

### Client Scope Mappers

- **Awx**
  - `aud`: Audience
  - `email`: User Attribute
  - `user_name`: User Attribute
  - `first_name`: User Attribute
  - `last_name`: User Attribute
  - Scope: `awx_users`

- **Awx-admin**
  - `is_org_admin`: `Hardcoded attribute` with organization name value
  - Scope: `awx_administrators`
