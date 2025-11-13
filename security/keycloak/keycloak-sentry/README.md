# Sentry+Keycloak SAML

Tested on Sentry 23.8.0, Keycloak 26.3
**Sentry doesn't allow role/group mapping via SAML2**. New users will use the default role, while existing users will remain the same.
**Sentry doesn't allow multiple authentication methods**. When SAML2 authentication via Keycloak is enabled, this option will be the only option available in the login page.

**Table of Contents:**
- [References](#references)
- [Sentry Setup](#sentry-setup)
- [Keycloak Setup](#keycloak-setup)
  - [Client](#client)
  - [Client Scope Mappers](#client-scope-mappers)
- [Author](#author)

## References

- [Configuring Sentry's SAML2 Provider with Keycloak](https://jayground8.github.io/blog/20250722-sentry-saml2)
- [Sentry. Custom SAML Provider](https://docs.sentry.io/organization/authentication/sso/saml2/)

## Sentry Setup

Go to `Settings > Auth > SAML2`
Identity Provider Metadata URL: `https://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM>/protocol/saml/descriptor` (`Realm settings > Endpoints`)
Attribute Mapping:
  - IdP User ID: `email`
  - User Email: `email`
  - First Name: `firstname`
  - Last Name: `lastname`
Next, you need to log into Keycloak to check the attribute mapping and link the current user.

## Keycloak Setup

Don't forget to map Keycloak groups and Client Scopes to corresponding Client Roles

### Client

- Client ID: `https://<SENTRY_HOSTNAME>/saml/metadata/sentry/` (works only with that id)
- Valid redirect URIs: `https://<SENTRY_HOSTNAME>/*`
- Name ID format: `email`
- Force name ID format: `Off`
- Force POST binding: `On`
- Sign documents: `On`
- Sign assertions: `On`
- SAML signature key name: `KEY_ID`
- Keys:
  - Client signature required: `Off`
- Client Roles:
  - `sentry_access` (for access only)

### Client Scope Mappers

- **Sentry**
  - `lastname`: X500 surname (lastName)
  - `email`: X500 email
  - `firstname`: X500 givenName (firstName)
  - Scope: `sentry_access`

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
