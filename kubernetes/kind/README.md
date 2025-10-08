# Kind Local Cluster

##  Reference
- [Kind Quick Start](https://kind.sigs.k8s.io/docs/user/quick-start/)
- [How to Test Ingress in a kind cluster](https://dustinspecker.com/posts/test-ingress-in-kind/)

## Setup
- This cluster setup uses ingress ready `kind.config`
```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
    extraPortMappings: # connect host ports to container
      - containerPort: 80
        hostPort: 80
        protocol: TCP
      - containerPort: 443
        hostPort: 443
        protocol: TCP
```
- Install kind cluster
```bash
kind create cluster --name local-cluster --config kind.config --kubeconfig ~/.kube/kind-config.conf
```
- Stop kind cluster
```bash
docker stop local-cluster-control-plane
```
- Start kind cluster
```bash
docker start local-cluster-control-plane
```
- Delete kind cluster
```bash
kind delete cluster --name local-cluster
```
