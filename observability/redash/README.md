# Redash

**Table of Contents:**
- [References](#references)
- [Docker deploy](#docker-deploy)
- [Author](#author)

## References

- [Setting up a Redash Instance](https://redash.io/help/open-source/setup/)

## Docker deploy

- Go to project directory
```bash
cd observability/redash/
```
- Run `docker-compose.yaml`
```bash
docker compose up -d
```
- Initialize Redash database
```bash
docker compose run --rm server create_db
```
- Access with browser `http://localhost:5000`

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
