# ClickHouse

Basic ClickHouse deploy.

**Table of Contents:**
- [References](#references)
- [Kubernetes Deploy](#kubernetes-deploy)
- [Native Installation](#native-installation)
  - [RedHat (AlmaLinux)](#redhat-almalinux)
- [Basic Commands](#basic-commands)
- [Author](#author)

## References

- https://clickhouse.com/docs/install
- https://clickhouse.com/docs/interfaces/cli

## [Kubernetes Deploy](/database/clickhouse/k8s/)

## Native Installation

### RedHat (AlmaLinux)

1. Add RPM repository
```bash
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://packages.clickhouse.com/rpm/clickhouse.repo
```

2. Install ClickHouse server and client
```bash
sudo yum install -y clickhouse-server clickhouse-client

# specified version
sudo yum install -y clickhouse-server-22.8.7.34
```

3. Start ClickHouse server
```bash
sudo systemctl enable clickhouse-server
sudo systemctl start clickhouse-server
sudo systemctl status clickhouse-server
```

4. Connect via client
```bash
# --host <host>
# --port <port>
# --user <user>
# --password <password>
# --database <database>
# --query <query>
clickhouse-client # localhost:9000 user:default
```

## Basic Commands

- Show databases
```sql
SHOW DATABASES; -- \l
```
- Show tables
```sql
SHOW TABLES; -- \d
```
- Use database
```sql
USE database_name; -- \c <DATABASE>
```

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
