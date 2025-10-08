# Redis Insight Kubernetes Deploy

- Create namespace
```bash
kubectl create namespace redisinsight
```
- Deploy to cluster
```bash
cd database/redis/redisinsight/
kubectl apply -f k8s/ -n redisinsight
```
- Port forward
```bash
kubectl -n redisinsight port-forward deployment/redisinsight 5540:5540
```
- Access with web browser `http://localhost:5540`

- Delete
```bash
kubectl delete namespace redisinsight
```

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
