# RabbitMQ

- [References](#references)
- [Docker Deploy](#docker-deploy)
  - [RabbitMQ 4.x + RabbitMQ Management](#rabbitmq-4x--rabbitmq-management)
  - [RabbitMQ 4.x + RabbitMQ Management + config files](#rabbitmq-4x--rabbitmq-management--config-files)
  - [Docker Compose Deploy](#docker-compose-deploy)
- [Native Install](#native-install)
  - [RedHat (AlmaLinux)](#redhat-almalinux)
- [Configuring](#configuring)
  - [RabbitMQ Management plugin](#rabbitmq-management-plugin)
  - [RabbitMQ Setup with Keycloak as OAuth 2.0 server](#rabbitmq-setup-with-keycloak-as-oauth-20-server)
- [Author](#author)


## References

- [Installing on RPM-based Linux (RHEL, CentOS Stream, Fedora, Amazon Linux 2023)](https://www.rabbitmq.com/docs/install-rpm)
- https://www.rabbitmq.com/docs/download
- https://hub.docker.com/_/rabbitmq/

## Docker Deploy

### RabbitMQ 4.x + RabbitMQ Management

- Start Docker container
```bash
docker run -d \ 
  --name rabbitmq \
  -p 5672:5672 \
  -p 15672:15672 \
  rabbitmq:4-management
```

### RabbitMQ 4.x + RabbitMQ Management + config files

- Go to the project directory
```bash
cd message-broker/rabbitmq
```
- Start Docker container
```bash
docker run -d \ 
  --name rabbitmq \
  -p 5672:5672 \
  -p 15672:15672 \
  -v ./rabbitmq.conf:/etc/rabbitmq/rabbitmq.conf \
  -v ./enabled_plugins:/etc/rabbitmq/enabled_plugins \
  rabbitmq:4-management
```

### Docker Compose Deploy

- Go to the project directory
```bash
cd message-broker/rabbitmq
```
- Run Docker Compose
```bash
docker compose up -d
```

## Native Install

### RedHat (AlmaLinux)

- Add RabbitMQ repo to `/etc/yum.repos.d/rabbitmq.repo`
```ini
##
## Zero dependency Erlang RPM
##

[modern-erlang]
name=modern-erlang-el9
# Use a set of mirrors maintained by the RabbitMQ core team.
# The mirrors have significantly higher bandwidth quotas.
baseurl=https://yum1.rabbitmq.com/erlang/el/9/$basearch
        https://yum2.rabbitmq.com/erlang/el/9/$basearch
repo_gpgcheck=1
enabled=1
gpgkey=https://github.com/rabbitmq/signing-keys/releases/download/3.0/cloudsmith.rabbitmq-erlang.E495BB49CC4BBE5B.key
gpgcheck=1
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
metadata_expire=300
pkg_gpgcheck=1
autorefresh=1
type=rpm-md

[modern-erlang-noarch]
name=modern-erlang-el9-noarch
# Use a set of mirrors maintained by the RabbitMQ core team.
# The mirrors have significantly higher bandwidth quotas.
baseurl=https://yum1.rabbitmq.com/erlang/el/9/noarch
        https://yum2.rabbitmq.com/erlang/el/9/noarch
repo_gpgcheck=1
enabled=1
gpgkey=https://github.com/rabbitmq/signing-keys/releases/download/3.0/cloudsmith.rabbitmq-erlang.E495BB49CC4BBE5B.key
       https://github.com/rabbitmq/signing-keys/releases/download/3.0/rabbitmq-release-signing-key.asc
gpgcheck=1
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
metadata_expire=300
pkg_gpgcheck=1
autorefresh=1
type=rpm-md


##
## RabbitMQ Server
##

[rabbitmq-el9]
name=rabbitmq-el9
baseurl=https://yum2.rabbitmq.com/rabbitmq/el/9/$basearch
        https://yum1.rabbitmq.com/rabbitmq/el/9/$basearch
repo_gpgcheck=1
enabled=1
# Cloudsmith's repository key and RabbitMQ package signing key
gpgkey=https://github.com/rabbitmq/signing-keys/releases/download/3.0/cloudsmith.rabbitmq-server.9F4587F226208342.key
       https://github.com/rabbitmq/signing-keys/releases/download/3.0/rabbitmq-release-signing-key.asc
gpgcheck=1
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
metadata_expire=300
pkg_gpgcheck=1
autorefresh=1
type=rpm-md

[rabbitmq-el9-noarch]
name=rabbitmq-el9-noarch
baseurl=https://yum2.rabbitmq.com/rabbitmq/el/9/noarch
        https://yum1.rabbitmq.com/rabbitmq/el/9/noarch
repo_gpgcheck=1
enabled=1
# Cloudsmith's repository key and RabbitMQ package signing key
gpgkey=https://github.com/rabbitmq/signing-keys/releases/download/3.0/cloudsmith.rabbitmq-server.9F4587F226208342.key
       https://github.com/rabbitmq/signing-keys/releases/download/3.0/rabbitmq-release-signing-key.asc
gpgcheck=1
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
metadata_expire=300
pkg_gpgcheck=1
autorefresh=1
type=rpm-md
```
- Update package metadata
```bash
dnf update -y
```
- Install RabbitMQ
```bash
dnf install -y rabbitmq-server
```
- Start service
```bash
systemctl start rabbitmq-server
systemctl status rabbitmq-server
```

- *Add firewall rules*
```bash
firewall-cmd --permanent --add-port=15672/tcp  # Web interface
firewall-cmd --permanent --add-port=5672/tcp   # AMQP protocol
firewall-cmd --reload
```

## Configuring

### RabbitMQ Management plugin

- Install Management plugin
```bash
rabbitmq-plugins enable rabbitmq_management
systemctl restart rabbitmq-server
systemctl status rabbitmq-server
```
- Add admin user
```bash
# Create admin user with "admin" password
rabbitmqctl add_user admin qwerty
# Grant admin privileges
rabbitmqctl set_user_tags admin administrator
# Grant all permissions
rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"
```
- Access with web browser `http://localhost:15672`

### [RabbitMQ Setup with Keycloak as OAuth 2.0 server](/security/keycloak/keycloak-rabbitmq/README.md)

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
