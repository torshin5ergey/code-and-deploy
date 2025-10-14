# RabbitMQ+Keycloak Connect OIDC

Tested on RabbitMQ 4.1.4, Keycloak 26.3

## References

- [Troubleshooting OAuth 2](https://www.rabbitmq.com/docs/troubleshooting-oauth2)
- [OAuth 2.0 Authentication Backend](https://www.rabbitmq.com/docs/oauth2#variables-configurable)

## Rabbitmq setup

- Install `rabbitmq_auth_backend_oauth2` plugin
```bash
rabbitmq-plugins enable rabbitmq_auth_backend_oauth2
```
- Setup Keycloak connect in [`/etc/rabbitmq/rabbitmq.conf`](/security/keycloak/keycloak-rabbitmq/rabbitmq.conf)
```ini
# log.console = true
# log.console.level = debug

auth_backends.1 = rabbit_auth_backend_oauth2
auth_backends.2 = rabbit_auth_backend_internal # basic auth

management.oauth_enabled = true
management.oauth_client_id = <KEYCLOAK_CLIENT_ID>
management.oauth_client_secret = <KEYCLOAK_CLIENT_SECRET>
management.oauth_provider_url = https://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM>
management.oauth_scopes = openid profile
management.oauth_disable_basic_auth = false # enable basic auth form

auth_oauth2.resource_server_id = <KEYCLOAK_CLIENT_ID>
auth_oauth2.preferred_username_claims.1 = preferred_username
auth_oauth2.additional_scopes_key = extra_scope
auth_oauth2.issuer = https://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM>
auth_oauth2.https.hostname_verification = wildcard
```

## Keycloak Setup

Don't forget to map Keycloak groups and Client Scopes to corresponding Client Roles

### Client

- Client ID: `rabbitmq`
- Valid redirect URIs: `https://<RABBITMQ_HOSTNAME>/*`
- Web origins: `https://<RABBITMQ_HOSTNAME>`
- Admin URL: `https://<RABBITMQ_HOSTNAME>`
- Client authentication: `On`
- Authorizations: `Off`
- Authentication flow: `Standard flow`, `Direct access grants`
- Client Roles:
  - `rabbitmq.tag:administrator` (ClientID.tag:administrator)
  - `rabbitmq.tag:management` (ClientID.tag:management)

### Client Scope Mappers

- **Rabbitmq**
  - `aud`: Audience
  - `client roles`: User Client Role
  - Scope: `rabbitmq.tag:administrator`, `rabbitmq.tag:management`
