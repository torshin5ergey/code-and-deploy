# SonarQube+Keycloak Setup SAML

Tested on SonarQube Community Build
v25.10.0.114319, Keycloak 26.3

## References

- https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/how-to-set-up-keycloak
- https://community.sonarsource.com/t/migrate-saml-to-local/120571
- https://community.sonarsource.com/t/how-to-transfer-ldap-users-to-local-users/119761

## SonarQube Setup

- Go to Administration > Authentication > SAML
- Add SAML configuration
  - Application ID: `sonarqube`
  - Provider Name: `Keycloak`
  - Provider ID: `https://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM>`
  - SAML login url: `https://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM>/protocol/saml`
  - Identity provider certificate: `ds:X509Certificate on https://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM>/protocol/saml/descriptor`
  - SAML user login attribute: `login`
  - SAML user name attribute: `name`
  - SAML user email attribute: `email`
  - SAML group attribute: `roles`
  - Sign requests: `Off`
  - Service provider private key: `empty`
  - Service provider certificate: `empty`

## Keycloak Setup

Don't forget to map Keycloak groups and Client Scopes to corresponding Client Roles

### Client

- Client ID: `sonarqube`
- Valid redirect URIs: `https://<SONARQUBE_HOSTNAME>/oauth2/callback/saml`
- Name ID format: `username`
- Sign documents: `On`
- Sign assertions: `On`
- Client Roles:
  - `sonar_administrators`
  - `sonar_users`

### Client Scope Mappers

- **Sonarqube**
  - `name`: User Property (firstName)
  - `email`: User Property (email)
  - `login`: User Property (username)
  - `roles`: Role list
  - Scope: `sonar_administrators`, `sonar_users`
