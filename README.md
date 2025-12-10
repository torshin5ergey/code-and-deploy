# DevOps Hub

---

![GitHub](https://img.shields.io/github/license/torshin5ergey/code-and-deploy)
![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?logo=kubernetes&logoColor=white)
![Ansible](https://img.shields.io/badge/ansible-%231A1918.svg?logo=ansible&logoColor=white)
![ClickHouse](https://img.shields.io/badge/clickhouse-%23005571.svg?logo=clickhouse&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DC382D.svg?logo=redis&logoColor=white)
![Kind](https://img.shields.io/badge/kind-%23326ce5.svg?logo=kubernetes&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?logo=nginx&logoColor=white)

DevOps deploy templates and configurations

## Repo Structure

- [database](/database/)
  - [clickhouse](/database/clickhouse/)
  - [mongodb](/database/mongodb/)
  - [mysql](/database/mysql/)
  - [postgresql](/database/postgresql/)
  - [redis](/database/redis/)
    - [redisinsight](/database/redis/redisinsight/)
- [infrastructure](/infrastructure/)
  - [dnsmasq](/infrastructure/dnsmasq/)
  - [gitlab](/infrastructure/gitlab/)
  - [rocket.chat](/infrastructure/rocketchat/)
- [kubernetes](/kubernetes/)
  - [ansible awx](/kubernetes/ansible-awx/)
  - [efk](/kubernetes/efk/)
  - [ingress-nginx](/kubernetes/ingress-nginx/)
  - [kind](/kubernetes/kind/)
  - [kubeadm setup](/kubernetes/kubeadm-setup/)
  - [rancher](/kubernetes/rancher/)
- [message-broker](/message-broker/)
  - [rabbitmq](/message-broker/rabbitmq/)
- [monitoring](/monitoring/)
  - [grafana](/monitoring/grafana/)
- [observability](/observability/)
  - [opensearch](/observability/opensearch/)
  - [redash](/observability/redash/)
  - [sentry](/observability/sentry/)
- [security](/security/)
  - [keycloak](/security/keycloak/)
  - [passwork]()
- [webserver](/webserver/)
  - [nginx](/webserver/nginx/)

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
