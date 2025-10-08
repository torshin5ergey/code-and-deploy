# Redis Insight

## References

- [Install Redis Insight](https://redis.io/docs/latest/operate/redisinsight/install/)
- [redis/redisinsight Dockerhub](https://hub.docker.com/r/redis/redisinsight)
- [Redis Insight configuration settings](https://redis.io/docs/latest/operate/redisinsight/configuration/)
- [Unable to import JSON config for redis connections. Issue #4571. Redis Insight Github](https://github.com/RedisInsight/RedisInsight/issues/4571)

## Docker Deploy

### Basic deploy

- Run Docker container
```bash
docker run -d \
  --name redisinsight \
  -p 5540:5540 \
  redis/redisinsight
```
- Access with web browser `http://localhost:5540`

### Preconfigured connections deploy

- Run Docker container
```bash
docker run -d \
  --name redisinsight \
  -p 5540:5540 \
  -e RI_PRE_SETUP_DATABASES_PATH=/db/connections.json \
  -v ~/devops-hub/database/redis/redisinsight/connections.json:/db/connections.json \
  redis/redisinsight
```
- Access with web browser `http://localhost:5540`

## [Kubernetes Deploy](/database/redis/redisinsight/k8s/)

## Configuration

### Environment Variables

- `RI_STDOUT_LOGGER`: Logs to stdout
  `true` | `false`
- `RI_LOG_LEVEL`: Log level
  `debug` | `warn` | `info`

### Preconfigure database connections

- Setup path to a JSON file containing the database connections to preconfigure with `RI_PRE_SETUP_DATABASES_PATH` environment variable
- Create `connections.json` and place in `/db/connections.json`
```json
[
  ...
  {
    "id": "redis-host", // unique connection id
    "name": "redis-host", // database alias
    "host": "redis-host.infra", // or IP
    "port": 6379,
    "username": "default",
    "password": "",
    "db": 1,
    "tls": false
  },
  ...
]
```

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
