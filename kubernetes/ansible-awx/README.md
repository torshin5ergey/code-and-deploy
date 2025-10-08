# Ansible AWX in Kubernetes

Basic AWX (Ansible Tower) Kubernetes deployment with local Persistent Volume in Minikube using official AWX Operator.

## References

- https://github.com/ansible/awx
- https://ansible-community.github.io/awx-operator-helm/

## Requirements

- Kubernetes кластер (тестировано на Minikube)
- Доступ к `kubectl`
- Helm installed

## Deploying

1. Add and install AWX Operator
```bash
# add awx helm repo
helm repo add awx-operator https://ansible-community.github.io/awx-operator-helm/
# install awx operator chart
helm install awx-operator awx-operator/awx-operator --create-namespace -n awx
```

2. Prepare storage (for minikube)
```bash
# connecto to minikube
minikube ssh
# create storage
mkdir /mnt/awx-storage
chown -R 26:26 /mnt/awx-storage # uid/gid 26 postgres user/group in container
chmod -R 750 /mnt/awx-storage
```

3. Apply manifests
```bash
kubectl apply -f .
kubectl get pods -n awx -w
```

4. Get access and credentials
```bash
# get minikube ip
minikube ip
# get service description (nodeport)
kubectl get svc ansible-awx-service -n awx

# get admin password
kubectl get secret ansible-awx-admin-password -o jsonpath="{.data.password}" -n awx | base64 --decode ; echo
```

5. Login
`<minikube ip>:<nodeport>`
username: `admin`
password: `<adminpassword>`

- To uninstall
```bash
kubectl delete ns awx
```
