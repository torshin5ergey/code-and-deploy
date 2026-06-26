# Keycloak+Rancher OIDC

Tested on Rancher 2.9.3, Keycloak 26.3

## Reference

- [Configure Keycloak (OIDC)](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/authentication-permissions-and-global-configuration/authentication-config/configure-keycloak-oidc)

## Rancher setup

Go to `Users & Authentication > Auth Provider > Keycloak`
- Client ID: `rancher`
- Client Secret: `<KEYCLOAK_CLIENT_SECRET>`
- Scopes: openid, Rancher
- Endpoints. You can use **Generate** to fill these endpoints automatically from the Keycloak URL and realm name, or **Specify** them manually. If your Keycloak uses slightly different paths, it’s safer to enter the URLs yourself. You can get the exact values from your realm’s OpenID configuration `https://<KEYCLOAK_HOSTNAME>/realms/<REALM>/.well-known/openid-configuration`
  - Rancher URL: `https://<RANCHER_HOSTNAME>/verify-auth`
  - Issuer: `https://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM>`
  - Auth Endpoint: `https://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM>/protocol/openid-connect/auth`

## Keycloak Setup

Don't forget to map Keycloak groups and Client Scopes to corresponding Client Roles

### Client

- Client ID: `rancher`
- Valid redirect URIs: `https://<RANCHER_HOSTNAME>/verify-auth`
- Web origins: `https://<RANCHER_HOSTNAME>`
- Admin URL: `https://<RANCHER_HOSTNAME>`
- Client authentication: `On`
- Authorization: `Off`
- Authentication flow: `Standard flow`, `Direct access grants`
- Client Roles:
  - `rancher_admins`
  - `rancher_users`

### Client Scope Mappers

- **Rancher**
  - `aud`: Audience
  - `email`: User Attribute
  - `preferred_username`: User Attribute
  - ``groups`: User Client Role (map client roles as user groups)
  - Scope: `rancher_admins`, `rancher_users`
