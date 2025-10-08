# EFK (Elasticsearch/Fluentd/Kibana)

Basic EFK Kubernetes deployment with local Persistent Volume in Minikube.

## References

- https://www.digitalocean.com/community/tutorials/how-to-set-up-an-elasticsearch-fluentd-and-kibana-efk-logging-stack-on-kubernetes

## Requirements

- Kubernetes cluster(Minikube)
- `kubectl` access

## Deploy

### Automatic

1. Check config [`03-fluent-cm.yaml`](/kubernetes/efk/fluentd/03-fluentd-cm.yaml) and [`04-fluentd-ds.yaml`](/kubernetes/efk/fluentd/04-fluentd-ds.yaml)
2. Prepare storage (minikube example)
- Create storage directory
```bash
# connect to minikube
minikube ssh
# create storage
mkdir /mnt/data-elasticsearch
chown -R 1000:1000 /mnt/data-elasticsearch
chmod -R 755 /mnt/data-elasticsearch
```
- Change path to directory in [`01-elasticsearch-pv.yaml`](/kubernetes/efk/elasticsearch/02-elasticsearch-pv.yaml)
3. Run deploy script from this directory
```bash
./efk-install.sh
```

### Step-by-Step
1. Create ns
```bash
kubectl apply -f 00-namespace.yaml
```

2. Prepare storage (for minikube)
```bash
# connect to minikube
minikube ssh
# create storage
mkdir /mnt/data-elasticsearch
chown -R 1000:1000 /mnt/data-elasticsearch
chmod -R 755 /mnt/data-elasticsearch
```

3. Deploy Elasticsearch
```bash
kubectl apply -f elasticsearch/
# check status
kubectl rollout status statefulset es-cluster -n efk-logging
```

4. Deploy Kibana
```bash
kubectl apply -f kibana/
# check status
kubectl rollout status deploy kibana -n efk-logging
```

5. Deploy Fluentd
Check config
```bash
kubectl apply -f fluentd/
# chack status
kubectl rollout status daemonset fluentd -n efk-logging
```

6. Get access and credentias
```bash
# get kibana nodeport
kubectl get svc kibana-nodeport -n efk-logging -o jsonpath='{.spec.ports[0].nodePort}'

# get node ip
kubectl get node <node-name> -o jsonpath='{.status.addresses[?(@.type=="InternalIP")].address}'
# or
minikube ip
```

7. Login
`<nodeip>:<nodeport>`
