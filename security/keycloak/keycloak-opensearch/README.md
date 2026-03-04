# Opensearch Dashboards+Keycloak Connect OIDC

Tested on Opensearch Dashboards 3.2.0, Keycloak 26.3

## References

- [Opensearch. OpenID Connect](https://docs.opensearch.org/latest/security/authentication-backends/openid-connect/)
- [Configuring Dashboards sign-in for multiple authentication options](https://docs.opensearch.org/latest/security/configuration/multi-auth/)
- [OpenID Connect troubleshooting](https://docs.opensearch.org/2.14/troubleshoot/openid-connect/)
- [Applying changes to configuration files](https://docs.opensearch.org/latest/security/configuration/security-admin/)

## Opensearch setup

- `opensearch/config/opensearch-security/config.yml`
```yaml
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
          challenge: false
          config:
            subject_key: "preferred_username"
            roles_key: "roles"
            openid_connect_url: "https://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM>/.well-known/openid-configuration"
            client_id: "KEYCLOAK_CLIENT_ID" # opensearch-dashboard
            client_secret: "KEYCLOAK_CLIENT_SECRET"
...
```
- `opensearch-dashboards/config/opensearch_dashboards.yml`
```yaml
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

- After editing `opensearch/config/opensearch-security/config.yml`, you must load the updated configuration into the system index `.opendistro_security` using the `securityadmin.sh` script. Even restarting with `systemctl restart opensearch` won't apply the changes. **The `securityadmin.sh` script updates the security configuration across all cluster nodes without requiring a node restart**.
```bash
# -bash: ./plugins/opensearch-security/tools/securityadmin.sh: Permission denied
chmod +x plugins/opensearch-security/tools/securityadmin.sh
# WARNING: nor OPENSEARCH_JAVA_HOME nor JAVA_HOME is set, will use
export OPENSEARCH_JAVA_HOME=/usr/share/opensearch/jdk

# backup current configs
:opensearch ./plugins/opensearch-security/tools/securityadmin.sh -backup /usr/share/opensearch/config/opensearch-security-backup -icl -nhnv -h localhost -cacert /usr/share/opensearch/config/root-ca.pem -cert /usr/share/opensearch/config/kirk.pem -key /usr/share/opensearch/config/kirk-key.pem

# for one file only -f file
:opensearch ./plugins/opensearch-security/tools/securityadmin.sh -f opensearch/config/opensearch-security/config.yml -icl -nhnv -cacert /usr/share/opensearch/config/root-ca.pem -cert /usr/share/opensearch/config/kirk.pem -key /usr/share/opensearch/config/kirk-key.pem

# for all config files in -cd path
:opensearch ./plugins/opensearch-security/tools/securityadmin.sh -cd /usr/share/opensearch/config/opensearch-security/ -icl -nhnv -cacert /usr/share/opensearch/config/root-ca.pem -cert /usr/share/opensearch/config/kirk.pem -key /usr/share/opensearch/config/kirk-key.pem
```
On error like `ERR: "CN=admin,O=internal.example.com" is not an admin user` list the DN of the admin certificate in `opensearch.yml`
```yaml
# opensearch/config/opensearch.yml
...
plugins.security.authcz.admin_dn:
  - CN=admin,O=internal.example.com
...
```

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

## Troubleshoot

- `{“statusCode”:401,“error”:“Unauthorized”,“message”:“Unauthorized”}`
Check the `challenge` setting for authc methods in `opensearch/config/opensearch-security/config.yml`. In my case, setting `challenge: false` for `basic_internal_auth_domain` resolved the issue.
