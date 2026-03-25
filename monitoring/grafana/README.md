# Grafana

Basic Keycloak install|deploy.

**Table of Contents:**

## References- [Grafana](#grafana)
- [References- Grafana](#references--grafana)
- [Docker Deploy](#docker-deploy)
- [Author](#author)

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
