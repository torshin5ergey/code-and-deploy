
# ClickHouse 26.5.1.68

FROM alpine:3.22 AS builder

WORKDIR /usr/bin

RUN apk add --no-cache curl bash

RUN curl https://clickhouse.com/ | sh && \
  ./clickhouse install

FROM alpine:3.22 AS final

LABEL author="Sergey Torshin @torshin5ergey" \
  description="Basic clickhouse-client Docker image. CodeAndDeploy"

COPY --from=builder /usr/bin/clickhouse-client /usr/bin/clickhouse-client

ENTRYPOINT [ "clickhouse-client" ]
CMD [ "--help" ]
