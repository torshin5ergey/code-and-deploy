# GitLab+Keycloak Setup OIDC

Tested on GitLab 18.3.1-ce

## References

- https://docs.gitlab.com/administration/auth/oidc/
- https://docs.gitlab.com/integration/omniauth/#supported-providers
- https://forum.gitlab.com/t/connecting-gitlab-with-keycloak/125361/5
- https://docs.truedev.ru/CI-CD/Gitlab/gitlab-auth-using-keycloak-oidc/#gitlab

## GitLab Setup

For Docker deploy
```yaml
...
...
    environment:
      GITLAB_OMNIBUS_CONFIG: |
        ...
        # Keycloak OIDC
        gitlab_rails['omniauth_enabled'] = true
        gitlab_rails['omniauth_allow_single_sign_on'] = ['openid_connect']
        gitlab_rails['omniauth_auto_link_ldap_user'] = true # merge with ldap users
        gitlab_rails['omniauth_auto_link_user'] = true # merge with basic user
        gitlab_rails['omniauth_block_auto_created_users'] = false

        gitlab_rails['omniauth_providers'] = [
          {
            name: "openid_connect",
            label: "Login with Keycloak", # button text
            # icon: "<CUSTOM_PROVIDER_ICON>",
            args: {
              name: "openid_connect",
              scope: ["openid", "Gitlab"],
              response_type: "code",
              issuer: "https://<KEYCLOAK_HOST>/realms/<KEYCLOAK_REALM>",
              discovery: true,
              client_auth_method: "query",
              uid_field: "preferred_username",
              # send_scope_to_token_endpoint: false,
              pkce: true,
              client_options: {
                identifier: "gitlab",
                secret: "<KEYCLOAK_CLIENT_SECRET>",
                redirect_uri: "https://<GITLAB_HOST>/users/auth/openid_connect/callback"
              }
            }
          }
        ]
        ...
...
```

## Keycloak Client Setup

Don't forget to map Keycloak groups and Client Scopes to corresponding Client Roles

### Client

- Client ID: `gitlab`
- Valid redirect URIs: `https://<GITLAB_HOSTNAME>/*`
- Valid post logout redirect URIs: `https://<GITLAB_HOSTNAME>/*`
- Root URL: `https://<GITLAB_HOSTNAME>`
- Home URL: `https://<GITLAB_HOSTNAME>`
- Web Origins: `https://<GITLAB_HOSTNAME>/*`
- Admin URL: `https://<GITLAB_HOSTNAME>`
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
  - `fitrstname`: User Attribute (firstName)
  - `lastname`: User Attribute (lastName)
  - Scope: `gitlab_users`
