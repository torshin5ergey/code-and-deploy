# Opensearch Dashboards+Keycloak Connect OIDC

Tested on Opensearch Dashboards 3.2.0, Keycloak 26.3

## References

- https://docs.opensearch.org/latest/security/authentication-backends/openid-connect/
- https://docs.opensearch.org/latest/security/configuration/multi-auth/

## Opensearch setup

- `config.yml`
```ini
...
config:
  dynamic:
    authc:
      ...
      oidc_auth_domain:
        description: "Authenticate via OIDC (OpenID Connect)"
        http_enabled: true
        transport_enabled: true
        order: 1
        http_authenticator:
          type: "openid"
          challenge: true
          config:
            subject_key: "preferred_username"
            roles_key: "roles"
            openid_connect_url: "https://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM>/.well-known/openid-configuration"
            client_id: "KEYCLOAK_CLIENT_ID" # opensearch-dashboard
            client_secret: "KEYCLOAK_CLIENT_SECRET"
...
```
- `opensearch_dashboards.yml`
```ini
...
# Keycloak OIDC
opensearch_security.auth.type: ["openid", "basicauth"] # enable both auth methods
opensearch_security.auth.multiple_auth_enabled: true

opensearch_security.openid.connect_url: "https://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM>/.well-known/openid-configuration"
opensearch_security.openid.client_id: "<KEYCLOAK_CLIENT_ID>" # opensearch-dashboards
opensearch_security.openid.client_secret: "<KEYCLOAK_CLIENT_SECRET>"
opensearch_security.openid.base_redirect_url: "http://<OPENSEARCH_HOSTNAME>"
opensearch_security.openid.scope: "openid Opensearch-dashboards" # Opensearch-dashboards custom Client Scope
opensearch_security.ui.openid.login.buttonname: "Log in with Keycloak"
...
```
- `roles.yml`
- `roles_mapping.yml`

## Keycloak Setup

Don't forget to map Keycloak groups and Client Scopes to corresponding Client Roles

### Client

- Client ID: `opensearch-dashboards`
- Valid redirect URIs: `https://<OPENSEARCH_HOSTNAME>/*`
- Valid post logout redirect URIs: `https://<OPENSEARCH_HOSTNAME>/*`
- Web origins: `https://<OPENSEARCH_HOSTNAME>`
- Admin URL: `https://<OPENSEARCH_HOSTNAME>`
- Client authentication: `On`
- Authorizations: `Off`
- Authentication flow: `Standard flow`, `Direct access grants`
- Client Roles:
  - `opensearch_admin`
  - `opensearch_user`

### Client Scope Mappers

- **Opensearch-dashboards**
  - `aud`: Audience
  - `email`: User Attribute
  - `preferred_username`: User Attribute
  - `roles`: User Client Role
  - Scope: `opensearch_user`, `opensearch_admin`
