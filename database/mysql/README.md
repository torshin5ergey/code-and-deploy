# MySQL

Basic MySQL deploy.

**Table of Contents:**
- [References](#references)
- [Docker Deploy](#docker-deploy)
- [Kubernetes Deploy](#kubernetes-deploy)
- [Configuration](#configuration)
- [Basic commands](#basic-commands)
- [Author](#author)

## References

- [mysql Dockerhub](https://hub.docker.com/_/mysql/)
- [mysql Command Line Client](https://dev.mysql.com/doc/refman/8.4/en/mysql.html)

## Docker Deploy

- Run Docker container
```bash
docker run -d \
  --name mysql \
  -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=rootpassword \
  mysql
```
- Connect to DB
```bash
# From container
docker exec -it mysql bash -c "mysql -p"
# Enter root password
```

## [Kubernetes Deploy](/database/mysql/k8s/)

## Configuration

**Environment variables:**
- `MYSQL_ROOT_PASSWORD`: MySQL root user password (required)
- `MYSQL_DATABASE`: Create database during initialization
- `MYSQL_USER`: Create user during initialization
- `MYSQL_PASSWORD`: Create password for created user

**Volume-mounts:**
- `/var/lib/mysql`: Data
- `/etc/mysql/conf.d`: Custom configurations
- `/docker-entrypoint-initdb.d`: SQL init scripts (Docker and k8s)

## Basic commands

- Connection
```bash
mysql db_name
mysql --user=user_name --password=db_name
```
- Execute SQL script
```bash
mysql db_name < script.sql
```

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
