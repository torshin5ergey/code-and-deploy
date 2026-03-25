# Grafana

Basic Keycloak install|deploy.

**Table of Contents:**
- [References](#references)
- [Docker Deploy](#docker-deploy)
- [Author](#author)

## References

- [Run Grafana Docker image](https://grafana.com/docs/grafana/latest/setup-grafana/installation/docker/)
- [Docker Hub grafana/grafana](https://hub.docker.com/r/grafana/grafana/)

## Docker Deploy

- Run Docker container
```bash
docker run -d \
  --name cnd-grafana \
  -p 3000:3000 \
  grafana/grafana
```
- Access with web browser `http://localhost:3000` with `admin`:`admin`

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
