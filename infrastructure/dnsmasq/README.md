# Dnsmasq

**Table Of Contents**
- [Reference](#reference)
- [Docker Compose Setup](#docker-compose-setup)

## Reference

- [Dnsmasq - network services for small networks.](https://dnsmasq.org/doc.html)
- [jpillora/docker-dnsmasq](https://github.com/jpillora/docker-dnsmasq)

## Docker Compose Setup

- Go to the project directory
```bash
cd infrastructure/dnsmasq/
```
- Change config [`dnsmasq.conf`](/infrastructure/dnsmasq/dnsmasq.conf)
- Run container
```bash
docker compose up -d
```
- Access with browser `localhost:5380` with `admin:admin` credentials
