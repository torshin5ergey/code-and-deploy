# Nginx Kubernetes Deploy

- Create namespace
```bash
kubectl create namespace nginx
```
- Deploy to cluster
```bash
cd webserver/nginx
kubectl apply -f k8s/
```
- Port forward
```bash
kubectl -n nginx port-forward deployment/nginx 8080:8080
```
- Access with web browser `http://localhost:8080`

- Delete
```bash
kubectl delete namespace nginx
```

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
