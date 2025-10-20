# MongoDB

**Table of Contents**
- [References](#references)
- [Docker Deploy](#docker-deploy)
- [Author](#author)

## References

## Docker Deploy

- Run Docker container
```bash
docker run -d \
  --name mongodb \
  -p 27017:27017 \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=password \
  mongo:latest
```
- Access mongo inside the contaier
```bash
docker exec -it mongodb mongosh -u admin -p password
```

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
