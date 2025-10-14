# Grafana+Keycloak Setup OIDC

Tested on Grafana 9.2.1, Keycloak 26.3

## References

- https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-authentication/keycloak/
- https://itdraft.ru/2024/10/28/nastroyka-oauth-avtorizatsii-v-grafana-keycloak-roles/

## Grafana Setup

- `grafana.ini`
```ini
# Keycloak SSO setup
[auth.generic_oauth]
enabled = true
name = keycloak
allow_sign_up = true
client_id = <KEYCLOKA_CLIENT_ID> # grafana
client_secret = <KEYCLOAK_CLIENT_SECRET>
scopes = openid offline_access
email_attribute_path = email
login_attribute_path = preffered_username
name_attribute_path = name
auth_url = http://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM>/protocol/openid-connect/auth
token_url = http://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM>/protocol/openid-connect/token
api_url = http://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM>/protocol/openid-connect/userinfo
# map 'groups' in token with Grafana roles
role_attribute_path = contains(roles[*], 'grafana_admin') && 'Admin' || contains(roles[*], 'grafana_editor') && 'Editor' || contains(roles[*], 'grafana_viewer') && 'Viewer'
allow_assign_grafana_admin = true
use_refresh_token = true
```

## Keycloak Setup

Don't forget to map Keycloak groups and Client Scopes to corresponding Client Roles

### Client

- Client ID: `grafana`
- Valid redirect URIs: `https://<GRAFANA_HOSTNAME>/login/generic_oauth`
- Root URL: `https://<GRAFANA_HOSTNAME>`
- Home URL: `https://<GRAFANA_HOSTNAME>`
- Web Origins: `https://<GRAFANA_HOSTNAME>`
- Admin URL: `https://<GRAFANA_HOSTNAME>`
- Client authentication: `On`
- Authorizations: `Off`
- Authentication flow: `Standard flow`, `Direct access grants`
- Client Roles:
  - `grafana_admin`
  - `grafana_editor`
  - `grafana_viewer`

### Client Scope Mappers

**Grafana**
  - `aud`: Audience
  - `email`: User Attribute
  - `preferred_username`: User Attribute
  - `name`: User Attribute (firstName)
  - `roles`: User Client Role
  - Scope: `grafana_admin`, `grafana_editor`, `grafana_viewer`
