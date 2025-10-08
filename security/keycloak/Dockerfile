
FROM keycloak/keycloak:26.3 AS build

LABEL author="Sergey Torshin @torshin5ergey" \
  description="Basic Keycloak Docker image (MySQL, Health). CodeAndDeploy"

RUN /opt/keycloak/bin/kc.sh build \
  --features=token-exchange,admin-fine-grained-authz \
  --db=mysql \
  --health-enabled=true

FROM keycloak/keycloak:26.3

COPY --from=build /opt/keycloak/ /opt/keycloak/

ENTRYPOINT ["/opt/keycloak/bin/kc.sh"]
