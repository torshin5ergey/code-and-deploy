# Kubernetes `kubeadm` Setup

Ansible plabooks and manual steps to set up a Kubernetes lcuster using `kubeadm` with different configurations.

## References

- https://www.golinuxcloud.com/install-kubernetes-cluster-kubeadm-centos-8/
- https://www.golinuxcloud.com/calico-kubernetes/
- https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/
- https://kubernetes.io/docs/reference/networking/ports-and-protocols/
- https://youtu.be/wIZamzt7MkM?feature=shared

## Configurations

- Container Runtimes:
  - Docker
  - Containerd
- CNI Plugins
  - Weave Net
  - Calico

## Prerequisites

Ansible inventory with `controller`, `workers` groups.

Tested with:
- Ubuntu 22.04 Server nodes (1 master, N workers)
- Ansible 2.17.10
- Weave Net 2.8.1
- Calico 3.25

## Quickstart

- Setup [`inventory.ini`](/kubernetes/kubeadm-setup/inventory/inventory.ini)
- Customize variables in playbook [`cluster-init.yaml`](/kubernetes/kubeadm-setup/cluster-init.yaml) if needed (CRI: Docker, containerd; CNI: Weave Net, Calico)
- Run playbook
```bash
ansible-playbook kubernetes/kubeadm-setup/cluster-init.yaml
```
- Join nodes. The `kubeadm join` command is in `kubeadm_join.sh` inside `ansible_user` $HOME directory.

## Manual Installation

### Install common packages

- apt-transport-https
- ca-certificates
- curl
- gpg

### Disable Swap (all nodes)

```bash
# disable
swapoff -a

# check
free -m
```

### Enable Firewall

- Control plane:
	- `6443/tcp` Kubernetes API access
	- `2379:2380/tcp` etcd server client API
	- `10250/tcp` Kubelet API
	- `10259/tcp` kube-scheduler
	- `10257/tcp` kube-controller-manager
- Worker nodes:
  - `10250/tcp` kubelet API
  - `10256/tcp` kube-proxy
  - `30000:32767/tcp` NodePort Services
- All nodes:
  - `6783/tcp` Weave Net control port
  - `6783/udp` Weave Net data port
  - `6784/udp` Weave Net data Fast Datapath port
  - `6781/tcp` Weave Net metrics
  - `6782/tcp` Weave Net metrics
  - `179/tcp` Calico BGP

### Enable IPv4 Packer Forwarding (all nodes)

- Add IPv4 packet forwarding to sysctl configuration
```bash
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.ipv4.ip_forward = 1
EOF
```
- Apply parameter without reboot
```bash
sudo sysctl --system
```

- Verify parameter
```bash
sysctl net.ipv4.ip_forward
```

### Install container runtime (all nodes)

**Containerd example**. Ubuntu Docker Installation is [here](https://docs.docker.com/engine/install/ubuntu/)

- Install conttainerd
```bash
apt update
apt instal -y containerd
```

- Create containerd default configuration
```bash
containerd config default > /etc/containerd/config.toml
```

- Configure the systemd cgroup driver by adding this lines
```toml
[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc]
  ...
  [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]
    SystemdCgroup = true
```

- Apply changes
```bash
systemctl restart containerd
```

### Install Kubernetes components (`kubelet`, `kubeadm`, `kubectl` on all nodes)

- [Installing kubeadm, kubelet and kubectl. kubernetes.io](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#installing-kubeadm-kubelet-and-kubectl)

- Check `kubelet` service
```bash
systemctl status kubelet
```

### Initialize Control Plane

- Init a Kubernetes control plane node
```bash
sudo -i

# pull images before installing
kubeadm config images pull

# --pod-network-cidr=10.10.0.0/16 adressed range (can be used when installing with Calico)
kubeadm init
```

- **Аfter installation it is necessary to execute the commands that are specified in the `kubeadm init` output!**
- **Also save the `kubeadm join` command from `kubeadm join` output**

- Check installation
```bash
kubectl cluster-info
```

- Check the `INTERNAL-IP` field in the `kubectl get nodes -o wide`. It must be node IP. If no, add to `/var/lib/kubelet/kubeadm-flags.env` param
```bash
...
KUBELET_KUBEADM_ARGS="--node-ip=123.45.67.89 ..."
...

# restart kubelet
systemctl restart kubelet
```

### Install Pod Network Add-on Plugin (control plane)

#### Weave Net

Apply Weave Net manifest
```bash
kubectl apply -f https://github.com/weaveworks/weave/releases/download/v2.8.1/weave-daemonset-k8s.yaml
```

#### Calico

##### With manifest

```bash
kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
```

##### Manually

- Download Calico networking manifest
```bash
curl https://calico-v3-25.netlify.app/archive/v3.25/manifests/calico.yaml -O
```

- Assign pod CIDR (if not done previously) in `calico.yaml`
```yaml
...
- name: CALICO_IPV4POOL_CIDR
  values: "10.142.0.0/24"    # random subnet
...
```

- Install Calico Plugin
```bash
kubectl apply -f calico.yaml
```

- [Install](https://docs.tigera.io/calico/latest/operations/calicoctl/install) `calicoctl`. It is a tool that provides simple interface for general management of Calico configuration

##### Verify

```bash
kubectl run nginx --image=nginx --port=80

# check IP
kubectl get po -o wide
```

### Join Worker Nodes

- Run `kubeadm join` command from `kubeadm init` output
```bash
sudo -i

kubeadm join ...
```

If you have lost the `kubeadm join` command with the Token ID then you can generate a new one
```bash
kubeadm token create --print-join-command
```
