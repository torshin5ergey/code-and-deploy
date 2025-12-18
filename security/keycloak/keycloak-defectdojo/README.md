# DefectDojo+Keycloak Connect SAML

## References

- [DefectDojo SSO Configuration (OAuth, SAML)](https://docs.defectdojo.com/en/customize_dojo/user_management/configure_sso/#keycloak)

## DefectDojo Setup

`docker-compose.yaml`
```yaml
uwsgi:
  environment:
    DD_SESSION_COOKIE_SECURE: 'True'
    DD_CSRF_COOKIE_SECURE: 'True'
    DD_SECURE_SSL_REDIRECT: 'True'
    DD_SOCIAL_AUTH_KEYCLOAK_OAUTH2_ENABLED: 'True'
    DD_SOCIAL_AUTH_KEYCLOAK_PUBLIC_KEY: <KEYCLOAK_REALM_PUBLIC_KEY>
    DD_SOCIAL_AUTH_KEYCLOAK_KEY: <KEYCLOAK_CLIENT_ID>
    DD_SOCIAL_AUTH_KEYCLOAK_SECRET: <KEYCLOAK_CLIENT_SECRET>
    DD_SOCIAL_AUTH_KEYCLOAK_AUTHORIZATION_URL: 'http://<KEYCLOAK_HOST>/realms/<KEYCLOAK_REALM>/protocol/openid-connect/auth'
    DD_SOCIAL_AUTH_KEYCLOAK_ACCESS_TOKEN_URL: 'http://<KEYCLOAK_HOST>/realms/<KEYCLOAK_REALM>/protocol'
    # DD_SOCIAL_AUTH_KEYCLOAK_LOGIN_BUTTON_TEXT: customize the login button’s text caption
```

## Keycloak Client Setup

Don't forget to map Keycloak groups and Client Scopes to corresponding Client Roles

### Client

- Client ID: `defectdojo`
- Root URL: `https://<DEFECTDOJO_HOSTNAME>/`
- Home URL: `https://<DEFECTDOJO_HOSTNAME>`
- Valid redirect URIs: `https://<DEFECTDOJO_HOSTNAME>/*`
- Valid post logout redirect URIs: `https://<DEFECTDOJO_HOSTNAME>/logout`
- Web origins: `https://<DEFECTDOJO_HOSTNAME>`
- Admin URL: `https://<DEFECTDOJO_HOSTNAME>`
- Client authentication: `On`
- Authorization: `Off`
- Authentication flow: `Standard flow`, `Direct access grants`
- Client Roles:
  - `defectdojo-access`

### Client Scope Mappers

- **Defectdojo**
  - `aud`: Audience
  - `groups`: 	Group Membership
  - `roles`: 	User Client Role
  - Scope: `defectdojo-access`

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
