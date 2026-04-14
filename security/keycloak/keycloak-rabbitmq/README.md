# RabbitMQ + Keycloak Connect OIDC

Tested on RabbitMQ 4.1.4, 3.10.21 and Keycloak 26.3.
RabbitMQ does not create users in its internal database. RabbitMQ only decodes an access token provided by the client and authorizes a user based on the scopes found in the token.

## References

- [Troubleshooting OAuth 2](https://www.rabbitmq.com/docs/troubleshooting-oauth2)
- [OAuth 2.0 Authentication Backend](https://www.rabbitmq.com/docs/oauth2#variables-configurable)
- [Management Plugin](https://www.rabbitmq.com/docs/management)
- [[Keycloak] Access Refused when creating queues. GitHub Issue #15](https://github.com/rabbitmq/rabbitmq-oauth2-tutorial/issues/15)

## RabbitMQ setup

- Install `rabbitmq_auth_backend_oauth2` plugin
```bash
rabbitmq-plugins enable rabbitmq_auth_backend_oauth2
```
- Setup Keycloak connect in [`/etc/rabbitmq/rabbitmq.conf`](/security/keycloak/keycloak-rabbitmq/rabbitmq.conf)
```ini
# /etc/rabbitmq/rabbitmq.conf

# log.console = true
# log.console.level = debug

auth_backends.1 = rabbit_auth_backend_oauth2
auth_backends.2 = rabbit_auth_backend_internal # basic auth

management.oauth_enabled = true
management.oauth_client_id = <KEYCLOAK_CLIENT_ID> # rabbitmq
management.oauth_client_secret = <KEYCLOAK_CLIENT_SECRET>
management.oauth_provider_url = https://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM>
management.oauth_scopes = openid
# Enable basic auth form on login page
# Works only on v3.13 and later. For v3.12 or earlier only one auth method will be shown on Management UI
management.oauth_disable_basic_auth = false

auth_oauth2.resource_server_id = <KEYCLOAK_CLIENT_ID>  # rabbitmq
auth_oauth2.preferred_username_claims.1 = preferred_username
auth_oauth2.additional_scopes_key = roles
auth_oauth2.issuer = https://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM> # Only for v3.13 and later. Use jwks_url instead
# auth_oauth2.jwks_url = https://keycloak.dev.ctc.ru/realms/keycloak/protocol/openid-connect/certs
# Allows connection to Keycloak with a wildcard certificate (*.example.com)
# RabbitMQ can download JWKS and OpenID-configuration without the TLS hostname_check_failed error.
# auth_oauth2.https.hostname_verification = wildcard
```

## Keycloak Setup

Don't forget to map Keycloak groups and Client Scopes to corresponding Client Roles

### Client

- Client ID: `rabbitmq`
- Valid redirect URIs: `https://<RABBITMQ_HOSTNAME>/*`
- Web origins: `https://<RABBITMQ_HOSTNAME>`
- Admin URL: `https://<RABBITMQ_HOSTNAME>`
- Client authentication: `On`
- Authorization: `Off`
- Authentication flow: `Standard flow`, `Direct access grants`
- Client Roles:
  - `rabbitmq.tag:administrator` (ClientID.tag:administrator)
  - `rabbitmq.tag:management` (ClientID.tag:management)
  - `rabbitmq.read:*/*` (ClientID.read:*/*, read all resources, all vhosts) 
  - `rabbitmq.write:*/*` (ClientID.write:*/*, write to all resources, all vhosts)

### Client Scope Mappers

- **Rabbitmq**
  - `aud`: Audience
  - `preferred_username`: User Attribute (username)
  - `roles`: User Client Role
  - Scope: `rabbitmq.tag:administrator`, `rabbitmq.tag:management`, `rabbitmq.read:*/*`, `rabbitmq.write:*/*`

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
