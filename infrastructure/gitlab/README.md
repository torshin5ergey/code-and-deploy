# GitLab

## References

- [Install GitLab in a Docker container](https://docs.gitlab.com/install/docker/)
- [Разворачиваем GitLab за пару кликов](https://habr.com/ru/companies/otus/articles/904236/)
- [Integrate LDAP with GitLab](https://docs.gitlab.com/administration/auth/ldap/)
- [Reset user passwords](https://docs.gitlab.com/security/reset_user_password/?tab=Linux%20package%20(Omnibus))

## Docker Deploy

- Go to project directory and run docker-compose.yaml
```bash
cd infrastructure/gitlab/
mkdir gitlab-data
docker compose up -d
```
- Get the `root` password
```bash
docker exec -it gitlab bash -c "cat /etc/gitlab/initial_root_password"
```
- Access with browser `http://localhost:8928`

## Configuration

### LDAP

- Configure LDAP integrations using the following settings
For Docker deploy:
```yaml
...
    environment:
      GITLAB_OMNIBUS_CONFIG: |
        ...
        gitlab_rails['password_authentication_enabled_for_web'] = false # disable password authentication
        # LDAP
        gitlab_rails['ldap_enabled'] = true
        gitlab_rails['ldap_servers'] = {
          'main' => {
            'label' => 'LDAP',
            'host' => <LDAP HOST>,
            'port' => <LDAP PORT>,
            'uid' => 'uid',
            'bind_dn' => <BIND_DISTINGUISHED_NAME>, # admin
            'password' => <ADMIN_PASSWORD>, # admin
            'encryption' => 'plain',
            'verify_certificates' => true,
            'timeout' => 10,
            'active_directory' => false, # freeipa
            'user_filter' => '(!(nsAccountLock=TRUE))', # only active accounts
            'base' => <BASE_DISTINGUISHED_NAME>,
            'lowercase_usernames' => true,
            'retry_empty_result_with_code' => [80],
            'allow_username_or_email_login' => false,
            'block_auto_created_users' => false
          }
        }
        ...
...
```

### [Keycloak SSO](/security/keycloak/keycloak-gitlab/README.md)

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
