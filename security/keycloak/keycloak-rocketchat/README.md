# Rocket.Chat+Keycloak SAML

Tested on Rocket.Chat 7.5.1, Keycloak 26.3

**Table of Contents:**
- [References](#references)
- [Rocket.Chat Setup](#rocketchat-setup)
- [Keycloak Setup](#keycloak-setup)
  - [Client](#client)
  - [Client Scope Mappers](#client-scope-mappers)
- [Author](#author)

## References

- [Keycloak - SAML Setup Example](https://docs.rocket.chat/docs/keycloak)

## Rocket.Chat Setup

Go to `Administration > Workspace > Settings > SAML`
Connection:
- Enable: `On`
- Custom Provider: `keycloak`
- Custom Entry Point: `https://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM>/protocol/saml`
- IDP SLO Redirect URL: `https://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM>/protocol/saml`
- Custom Issuer: `https://<ROCKETCHAT_HOSTNAME>/_saml/metadata/<KEYCLOAK_REALM>`
- Configure certificates

## Keycloak Setup

Don't forget to map Keycloak groups and Client Scopes to corresponding Client Roles

### Client

- Client ID: `https://<ROCKETCHAT_HOSTNAME>/_saml/metadata/<KEYCLOAK_REALM>` (works only with that id)
- Valid redirect URIs: `https://<ROCKETCHAT_HOSTNAME>/_saml/validate/<KEYCLOAK_REALM>`
- Name ID format: `email`
- Sign documents: `On`
- Sign assertions: `On`
- SAML signature key name: `KEY_ID`
- Client Roles:
  - `rocketchat_user` (for access only)

### Client Scope Mappers

- **Rocketchat**
  - `cn`: User Attribute (firstName)
  - `email`: User Attribute
  - `username`: User Attribute (optional?)
  - Scope: `rocketchat_user`

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
