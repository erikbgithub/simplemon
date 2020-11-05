#!/bin/bash

# from: https://katacoda.com/bwplotka/courses/thanos

cat >> EOF >/tmp/example-prom.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s
  external_labels:
    cluster: eu1
    replica: 0

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['127.0.0.1:9090']
  - job_name: 'sidecar'
    static_configs:
      - targets: ['127.0.0.1:19091','127.0.0.1:19092']
EOF

docker run -d --net=host --rm \
    -v /tmp/example-prom.yml:/etc/prometheus/prometheus.yml \
    -v $(pwd)/prometheus0_eu1_data:/prometheus \  # TODO volume
    -u root \
    --name prometheus-0-eu1 \
    quay.io/prometheus/prometheus:v2.14.0 \
    --config.file=/etc/prometheus/prometheus.yml \
    --storage.tsdb.path=/prometheus \
    --web.listen-address=:9090 \
    --web.external-url=https://2886795311-9090-elsy05.environments.katacoda.com \
    --web.enable-lifecycle


docker run --rm quay.io/thanos/thanos:v0.13.0 --help

# TODO not reconfigured for usefulness
docker run -d --net=host --rm \
    -v $(pwd)/prometheus0_eu1.yml:/etc/prometheus/prometheus.yml \
    --name prometheus-0-sidecar-eu1 \
    -u root \
    quay.io/thanos/thanos:v0.13.0 \
    sidecar \
    --http-address 0.0.0.0:19090 \
    --grpc-address 0.0.0.0:19190 \
    --reloader.config-file /etc/prometheus/prometheus.yml \
    --prometheus.url http://127.0.0.1:9090 && echo "Started sidecar for Prometheus 0 EU1"

# TODO not reconfigured for usefulness
docker run -d --net=host --rm \
    --name querier \
    quay.io/thanos/thanos:v0.13.0 \
    query \
    --http-address 0.0.0.0:29090 \
    --query.replica-label replica \
    --store 127.0.0.1:19190 \
    --store 127.0.0.1:19191 \
    --store 127.0.0.1:19192 && echo "Started Thanos Querier"


