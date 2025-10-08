# Grafana Kubernetes Deploy

- Deploy to cluster
```bash
cd monitoring/grafana
kubectl create namespace grafana --dry-run=client -o yaml | kubectl apply -f - && kubectl apply -f k8s -n grafana
```
- Port forward
```bash
kubectl -n grafana port-forward deployment/grafana 3000:3000
```
- Access with web browser `http://localhost:3000`. Credentials `admin:admin`

- Delete
```bash
kubectl delete ns grafana
```

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
