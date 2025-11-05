# Rancher

**Table of Contents**
- [Reference](#reference)
- [Docker Deploy](#docker-deploy)
- [Kubernetes Deploy](#kubernetes-deploy)
- [Troubleshooting](#troubleshooting)
- [Author](#author)

## Reference

- [Rancher. Password Requirements]https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/resources/bootstrap-password#password-requirements
- [Rancher. Helm CLI Quick Start](https://ranchermanager.docs.rancher.com/getting-started/quick-start-guides/deploy-rancher-manager/helm-cli)
- [Github  cert-manager/cert-manager](https://github.com/cert-manager/cert-manager/releases/)
- [Github rancher/rancher issue Start rancher without ssl?!? #14063](https://github.com/rancher/rancher/issues/14063)
- [Github rancher/rancher issue [BUG] fatal: unable to access 'https://git.rancher.io/charts/': Could not resolve host: git.rancher.io #41636](https://github.com/rancher/rancher/issues/41636)

## Docker Deploy

- Deploy Rancher container
```bash
docker run -d \
  --name rancher \
  --privileged \
  -p 8080:80 -p 8443:443 \
  -v ./rancher_data:/var/lib/rancher \
  rancher/rancher:v2.9.3 \
  --restart=unless-stopped \
  --no-cacerts
```
- Get bootstrap password
```bash
docker logs rancher  2>&1 | grep "Bootstrap Password:"
```

## Kubernetes Deploy

- Prepare certificate management, ready for Rancher deploy
```bash
helm repo add rancher-latest https://releases.rancher.com/server-charts/latest

kubectl create namespace cattle-system

# v1.19.1
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.19.1/cert-manager.crds.yaml

helm repo add jetstack https://charts.jetstack.io

helm repo update

helm install cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace
```
- Install Rancher with Helm
```bash
# check versions available
helm search repo rancher-latest/rancher --versions

helm install rancher rancher-latest/rancher \
  --namespace cattle-system \
  --set hostname=rancher.local \
  --set replicas=1 \
  --set bootstrapPassword=administrator \
  --version 2.12.0
```
- Wait for `Running` state and optionally check bootstrap password
```bash
kubectl get po -n cattle-system -w

```
- Port forward
```bash
kubectl port-forward -n cattle-system svc/rancher 8443:443
```
- Access on `localhost:8443` with `administrator` bootstrap password

## Troubleshooting

```
[ERROR] error syncing 'library': handler catalog: Clone failed: Cloning into 'management-state/catalog-cache/380859f1003fe7603cddc6c15b34b7263f1f0deaa92ddcde425711d032ee7078'...
fatal: unable to access 'https://git.rancher.io/charts/': Could not resolve host: git.rancher.io
: exit status 128, requeuing
```
- Add DNS server into Rancher container
```bash
kubectl exec -it <RANCHER-POD> -n cattle-system -- bash -c "echo nameserver 8.8.8.8 >> /etc/resolv.conf"
```

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
