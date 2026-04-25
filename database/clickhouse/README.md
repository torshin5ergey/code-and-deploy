# ClickHouse

Basic ClickHouse deploy.

**Table of Contents:**
- [References](#references)
- [Kubernetes Deploy](#kubernetes-deploy)
- [Native Installation](#native-installation)
  - [RedHat (AlmaLinux)](#redhat-almalinux)
- [Clickhouse Server Migration](#clickhouse-server-migration)
- [Author](#author)

## References

- [Install ClickHouse | ClickHouse Docs](https://clickhouse.com/docs/install)
- [clickhousectl | ClickHouse Docs](https://clickhouse.com/docs/interfaces/cli)
- [Backup and restore in ClickHouse](https://clickhouse.com/docs/operations/backup/overview)
- [Altinity/clickhouse-backup | GitHub](https://github.com/Altinity/clickhouse-backup)
- [User Guide | Altinity/clickhouse-backup | DeepWiki](https://deepwiki.com/Altinity/clickhouse-backup/2-user-guide)
- [Moving ClickHouse to Another Server](https://kb.altinity.com/altinity-kb-setup-and-maintenance/altinity-kb-data-migration/rsync/)

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

# or download and install archived version
wget https://packages.clickhouse.com/repo-archive/rpm/stable/x86_64/clickhouse-common-static-20.9.2.20-2.x86_64.rpm
wget https://packages.clickhouse.com/repo-archive/rpm/stable/x86_64/clickhouse-server-20.9.2.20-2.noarch.rpm
wget https://packages.clickhouse.com/repo-archive/rpm/stable/x86_64/clickhouse-client-20.9.2.20-2.noarch.rpm
dnf install clickhouse-common-static-20.9.2.20-2.x86_64.rpm clickhouse-server-20.9.2.20-2.noarch.rpm clickhouse-client-20.9.2.20-2.noarch.rpm
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

## Clickhouse Server Migration

Methods:
1. Use native ClickHouse `BACKUP`-`RESTORE`. [reference](https://clickhouse.com/docs/operations/backup/overview)
2. Use Altinity `clickhouse-backup` tool (Upload to S3, Google Cloud Storage, Cloud Object Service, FTP, SFTP, ). [reference](https://github.com/Altinity/clickhouse-backup)
3. Run a full recursive sync of the data directory from the old server to the new one. [reference](https://kb.altinity.com/altinity-kb-setup-and-maintenance/altinity-kb-data-migration/rsync/)

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
