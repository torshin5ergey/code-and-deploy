# Keycloak

Basic Keycloak install/setup/deploy.

**Table of Contents:**
- [References](#references)
- [Native Install](#native-install)
  - [AlmaLinux 9.5 Minimal](#almalinux-95-minimal)
- [Docker deploy](#docker-deploy)
- [Basic Client setup](#basic-client-setup)
- [Tokens](#tokens)
  - [ID Token](#id-token)
  - [Access Token](#access-token)
- [Author](#author)

## References

- [Getting Started With Keycloak Identity Provider (free Identity Server alternative by Milan Jovanović)](https://www.youtube.com/watch?v=fvxQ8bW0vO8)
- [How do I create a permanent admin account in Keycloak 26.0.0?](https://github.com/keycloak/keycloak/discussions/33803)
- [All configuration](https://www.keycloak.org/server/all-config)
- [Keycloak Account Console Status Code: 403 Forbidden ](https://keycloak.discourse.group/t/status-code-403-forbidden/10854/2)
- [Keycloak OpenJDK](https://www.keycloak.org/getting-started/getting-started-zip)
- [Token Lifespan Configuration Guide](https://docs.expertflow.com/cx-knowledgebase/latest/keycloak-token-lifespan-configuration)

## Native Install

### AlmaLinux 9.5 Minimal

- Install OpenJDK 21
```bash
dnf install java-21-openjdk -y
```
- Download the latest release tar
```bash
curl -O -L https://github.com/keycloak/keycloak/releases/download/26.4.0/keycloak-26.4.0.tar.gz
```
- Extract tar.gz
```bash
tar -xzvf keycloak-26.4.0.tar.gz
```
- Run keycloak in dev mode
```bash
cd keycloak-26.4.0
bin/kc.sh start-dev
```
- Access on `http://localhost:8080/`

## Docker deploy

- Go to project directory
```bash
cd security/keycloak
```
- Build Docker container
```bash
docker build -t cnd-keycloak .
```
- Setup preferred databse and edit config parameters for database in `keycloak.conf`
- Run Docker container
```bash
docker run \
  --name cnd-keycloak \
  -p 8080:8080 \
  -v ./keycloak.conf:/opt/keycloak/conf/keycloak.conf:ro \
  cnd-keycloak \
  start --optimized
```
- Access with web browser `http://localhost:8080` with `bootstrap-admin:qwerty` credentials

**Basic dev deploy**

- Run Docker container
```bash
docker run -e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin -p 8080:8080 quay.io/keycloak/keycloak:26.3 start-dev
```
- Access with web browser `http://localhost:8080` with `admin:admin` credentials

## Basic Client setup

- **Valid redirect URIs**: `http://localhost:8000/`
  Only redirect the user to a URL that mathces a valid redirect URI on login
- **Valid post redirect URIs**: `http://localhost:8000/`
  Only redirect the user to a URL that mathces a valid redirect URI on logout
- **Web origins**: `http://localhost:8000/`
  Valid web origins of the application for CORS requests

## Tokens

### ID Token

The ID token is used by the application to establish the identity of the authenticated user

- `exp`
  Date and time the token expires in seconds since 01/01/1970 00:00:00 UTC
- `iss`
  Issuer of the token, Keycloak realm URL
- `sub`
  Authenticated user unique identifier
- `name`
  First and last name of the authenticated user
- `preferred_username`
  The username of the authenticated user

### Access Token

- `allowed-origins`
  A list of permitted web origins fo rthe application. Backend service can use this field when deciding wheter web origins should be peritted for CORS requests
- `realm_access`
  A list of global realm roles. Intersection between the roles granted to the user, and the roles the client has access to
- `resource_access`
  A list of client roles
- `scope`
  Can be used to decide what fields to include in the token and by backends to decide what APIs the token can access

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
