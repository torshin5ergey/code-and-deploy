
# PostgreSQL

Basic PostgreSQL deploy.

**Table of Contents:**
- [References](#references)
- [Docker Deploy](#docker-deploy)
- [Basic commands](#basic-commands)
- [Author](#author)

## References

- [postgres Dockerhub](https://hub.docker.com/_/postgres/)

## Docker Deploy

- Run Docker container
```bash
docker run -d \
  --name postgres \
  -p 5432:5432 \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=keycloak \
  postgres:16
```

- Connect to DB
```bash
docker exec -it postgres-keycloak bash -c "psql -U postgres"
```

## Basic commands

- Connection
```bash
psql -h <host(localhost)> -p <port(5432)> -U <username(current system username)> -d <database(current system username)>
```
- List databases
```
\l
```
- Connect to database
```
\c <database>
```
- List tables
```
\dt
```

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
