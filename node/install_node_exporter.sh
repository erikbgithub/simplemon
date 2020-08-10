#!/bin/bash

set -exuo pipefail

echo "TODO: OVERWRITE these vars if you have a different setup"
export OS="linux" # OPTIONS observed: darwin, linux, netbsd
export ARCH="amd64" # OPTIONS observed: 386, amd64, arm64, armv{5,6,7}, mips, mips64, mips64le, mipsle, ppc64, ppc64le, s390x

export LATEST_TAG=$(curl -v https://github.com/prometheus/node_exporter/releases/latest 2>&1 |awk -F'v' '/location: /{print $NF}'| tr -d '[:space:]')

export LATEST_URL="https://github.com/prometheus/node_exporter/releases/download/v${LATEST_TAG}/node_exporter-${LATEST_TAG}.${OS}-${ARCH}.tar.gz"
export SHA_URL="https://github.com/prometheus/node_exporter/releases/download/v${LATEST_TAG}/sha256sums.txt"

rm -rf /tmp/nodeexpdownload
mkdir -p /tmp/nodeexpdownload
pushd /tmp/nodeexpdownload
wget $LATEST_URL
wget $SHA_URL

echo "CHECKSUM"
grep "$(sha256sum node_exporter-*.tar.gz |awk '{print $1}')" sha256sums.txt

tar xvf node_exporter-*.tar.gz
mv node_exporter-*/node_exporter ~/.local/bin/node_exporter_${LATEST_TAG}
rm -rf ~/.local/bin/node_exporter
ln -s ~/.local/bin/node_exporter_${LATEST_TAG} ~/.local/bin/node_exporter

ls -al ~/.local/bin


popd
