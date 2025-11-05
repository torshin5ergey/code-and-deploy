# Rocket.Chat

**Table of Contents:**
- [References](#references)
- [Docker Compose Deploy](#docker-compose-deploy)
- [Author](#author)

## References

- [Rocket.Chat. Deploy with Docker & Docker Compose](https://docs.rocket.chat/v1/docs/deploy-with-docker-docker-compose)

## Docker Compose Deploy

- Go to the project directory
```bash
cd infrastructure/rocketchat/
```
- Clone official rocketchat repository
```bash
git clone --depth 1 https://github.com/RocketChat/rocketchat-compose.git
cd rocketchat-compose
```
- Configure deployment
```bash
cp .env.example .env
nano .env

# RELEASE=7.5.1
# DOMAIN=localhost
# ROOT_URL=http://localhost
```
- Run basic Docker containers setup
```bash
docker compose -f compose.database.yml -f compose.yml up -d
```
- Open `http://localhost:3000` and setup admin account and workspace

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
