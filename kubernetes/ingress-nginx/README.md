# Ingress Nginx Community Basic Deploy

## Reference

- [Ingress Nginx Controller Installation Guide](https://kubernetes.github.io/ingress-nginx/deploy/)

## Kubernetes Deploy
- Install Ingress nginx
```bash
helm upgrade --install ingress-nginx ingress-nginx \
  --repo https://kubernetes.github.io/ingress-nginx \
  --namespace ingress-nginx --create-namespace

# Install fo kind
kubectl apply --filename https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/static/provider/kind/deploy.yaml
```
