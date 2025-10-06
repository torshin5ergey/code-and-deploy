# MySQL Kubernetes Deploy

- Create namespace
```bash
kubectl create namespace mysql
```
- Deploy to cluster
```bash
cd database/mysql
kubectl apply -f k8s/ -n mysql
```
- Connect to database
```bash
# from pod
kubectl exec -it deploy/mysql -n mysql -- bash -c 'mysql -u root -p"$MYSQL_ROOT_PASSWORD"'

# Port-forward and connect to localhost:3306
kubectl -n mysql port-forward deployment/mysql 3306:3306
```

- Delete
```bash
kubectl delete namespace mysql
```

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
