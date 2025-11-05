# Redash+Keycloak Setup SAML

Tested on Redash 8.0.0, Keycloak 26.3

## References

- [Authentication Options (SSO, Google OAuth, SAML)](https://redash.io/help/user-guide/users/authentication-options/)

## Redash Setup

- Go to `Settings > General > Authentication` check `SAML Enabed`
    - SAML Metadata URL: `https://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM>/protocol/saml/descriptor`
    - SAML Entity ID: `redash`
    - SAML NameID Format: `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress` *(can be found in metadata .xml file)*

## Keycloak Setup

Don't forget to map Keycloak groups and Client Scopes to corresponding Client Roles

### Client

- Client ID: `https://<REDASH_HOSTNAME>/saml/callback?org_slug=default`
- Valid redirect URIs: `https://<REDASH_HOSTNAME>/saml/callback?org_slug=default`
- Valid post logout redirect URIs: `https://<REDASH_HOSTNAME>/`
- Name ID format: `email`
- Force name ID format: `On`
- Sign documents: `On`
- Sign assertions: `On`
- Client Roles:
  - `admin`
  - `redash_users`

### Client Scope Mappers

- **Awx**
  - `aud`: Audience
  - `RedashGroups`: Role list (Client roles will be mapped to groups)
  - `FirstName`: User Attribute
  - `LastName`: User Attribute
  - Scope: `redash_users`, `admin`

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
