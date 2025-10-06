## Kubernetes Deploy

- Create namespace
```bash
kubectl create namespace clickhouse
```
- Deploy to cluster
```bash
cd database/clickhouse/
kubectl apply -n clickhouse -f k8s/
```
- Test connect with clickhouse-client pod
```bash
kubectl exec -it clickhouse-client -n clickhouse -- bash
```

- Delete
```bash
kubectl delete namespace clickhouse
```

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
