# ClickHouse Client

**Table of Contents:**
- [References](#references)
- [Docker Deploy](#docker-deploy)
  - [Custom Docker Image](#custom-docker-image)
  - [ClickHouse Server Images](#clickhouse-server-images)
- [Author](#author)

## References

- [ClickHouse Client | ClickHouse Docs](https://clickhouse.com/docs/interfaces/client)
- [clickhouse | DockerHub](https://hub.docker.com/_/clickhouse)
- [yandex/clickhouse-client | DockerHub](https://hub.docker.com/r/yandex/clickhouse-client)

## Docker Deploy

### Custom Docker Image

- Build image
```bash
cd code-and-deploy/database/clickhouse/clickhouse-client

docker build -t clickhouse-client-cnd .
# run and connect
docker run --rm -it clickhouse-client-cnd --version
docker run --rm -it \
  clickhouse-client-cnd \
  --host <host> --database <database> --user <user> --password <password>
```

### ClickHouse Server Images

- Run ClickHouse container interactive
```bash
# clickhouse
# yandex/clickhouse-client
docker run --rm -it \
  --name clickhouse-client \
  --entrypoint bash \
  clickhouse
```
- Connect via `clickhouse-client`
```bash
clickhouse-client --host <host> --database <database> --user <user> --password <password>
```

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
