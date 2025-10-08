# Keycloak+MySQL Kubernetes Deploy

- Create namespace
```bash
kubectl create namespace keycloak
```
- Deploy to cluster
```bash
cd security/keycloak
kubectl apply -f k8s/ -n keycloak
```
- Port forward
```bash
kubectl -n keycloak port-forward deployment/keycloak 8080:8080
```
- Access with web browser `http://localhost:8080`
  username: `bootstrap-admin`
  password: `qwerty`

- Delete
```bash
kubectl delete namespace keycloak
```

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
