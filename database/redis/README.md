# Redis

Basic Redis deploy.

**Table of Contents:**
- [References](#references)
- [Docker Deploy](#docker-deploy)
- [Author](#author)

## References

- [redis Dockerhub](https://hub.docker.com/_/redis)
- [How to Deploy and Run Redis in a Docker Container](https://redis.io/tutorials/operate/orchestration/docker/)

## Docker Deploy

- Run simple Docker container
```bash
docker run -d \
  --name redis \
  -p 6379:6379 \
  redis
```
- Connect to DB
```bash
docker exec -it redis bash -c "redis-cli"
```

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
