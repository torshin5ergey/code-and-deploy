# Sentry

**Table of Contents:**
- [References](#references)
- [Docker deploy](#docker-deploy)
- [Author](#author)

## References

- [Self-Hosted Sentry](https://develop.sentry.dev/self-hosted/)
- [Sentry. Configuration and Authentication](https://docs.sentry.io/cli/configuration/)
- [Дружим Sentry Self-Hosted и LDAP](https://habr.com/ru/articles/691140/)

## Docker deploy

- Set version
```bash
VERSION=23.8.0
```
- Clone self-hosted repository
```bash
git clone https://github.com/getsentry/self-hosted.git
cd self-hosted
git checkout ${VERSION}
```
- Run install script
```bash
./install.sh
```
- Start Docker Compose (about 40 **!** containers for this version)
```bash
docker compose up -d
```
- You can create user during `install.sh` or with this command
```bash
docker compose exec web sentry createuser
```
- Access with browser `http://localhost:9000`

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
