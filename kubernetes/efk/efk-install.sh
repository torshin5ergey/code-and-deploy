#! /bin/bash
set -e

# ! CUSTOMIZE: node name
NODE_NAME=minikube

NODE_IP=$(kubectl get node $NODE_NAME -o jsonpath='{.status.addresses[?(@.type=="InternalIP")].address}')

# namespace
NAMESPACE=efk-logging
kubectl apply -f 00-namespace.yaml

# elasticsearch
kubectl apply -f elasticsearch
kubectl rollout status statefulset es-cluster --namespace=$NAMESPACE

# kibana
kubectl apply -f kibana
kubectl rollout status deploy kibana --namespace=$NAMESPACE
KIBANA_NODEPORT=$(kubectl get svc kibana-nodeport --namespace=$NAMESPACE -o jsonpath='{.spec.ports[?(@.name=="http")].nodePort}')

# fluentd
kubectl apply -f fluentd
kubectl rollout status daemonset fluentd --namespace=$NAMESPACE

echo "EFK has been successfully deployed!\nKibana available at http://$NODE_IP:$KIBANA_NODEPORT"
