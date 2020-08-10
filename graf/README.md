## Simple Grafana

Simple Grafana Setup to work well with Node Exporter and Prometheus
set up in the same repo.

The original idea was to load the dashboard and prometheus source via
the web API, but this didn't work out yet. Will leave the files in here
so it can be tried again later.

## Howto

TODO
(not up to date and not adapted from Prometheus to Grafana stuff.)

```
$ make install
$ systemctl --user restart simplegraf
$ systemctl --user status simplegraf
# hopefully something green
```

Then go to your browser and check out `http://localhost:3000`.

# Stats used

 *  CPU: Stat Graph with: `1 - (sum by (instance) (rate(node_cpu_seconds_total{mode="idle"}[3m]))) / (sum by (instance) (rate(node_cpu_seconds_total[3m])))`
   * Threshhold: Red 0.8, Yellow 0.6, Green
 * Mem: `((node_memory_MemTotal_bytes - node_memory_MemFree_bytes) / node_memory_MemTotal_bytes) * 100`
 * Disk: `(1 - (node_filesystem_avail_bytes / node_filesystem_size_bytes)) * 100`
 * Network: TODO
