# Simplemon

A simple monitoring example solution that integrates well with
[simpleserver](https://github.com/rhdojun/simpleserver).

Install it with: `make install` (which will call into the sub directories for you)

Run it with: `make run`


# Sources

The following articles have been used in the creation of this repo. Better
documentation is TODO, but in the mean time hopefully these can help:

 * [A blog series that convinced me that podman might be more interesting than docker](https://mkdev.me/en/posts/dockerless-part-3-moving-development-environment-to-containers-with-podman)
 * [Where metrics fit into Cluster Observability](https://techbeacon.com/enterprise-it/monitoring-demystified-guide-logging-tracing-metrics)
 * [Timeseries and PromQL basics](https://www.youtube.com/watch?v=hTjHuoWxsks)
 * [Explanation for the components of a PromQL Query](https://www.innoq.com/en/blog/prometheus-counters/#orderscreatedwithinthelast5minutes)
 * [Node Exporter + Prom install](https://www.linuxtechi.com/install-prometheus-monitoring-tool-centos-8-rhel-8/)
 * [Apache Exporter for Simpleserver](https://github.com/Lusitaniae/apache_exporter)
 * [Another Apache stats related article](https://www.tecmint.com/monitor-apache-web-server-load-and-page-statistics/)
 * [CPU Usage Metrics](https://www.robustperception.io/understanding-machine-cpu-usage)
 * [Disk Usage Metrics](https://devconnected.com/monitoring-disk-i-o-on-linux-with-the-node-exporter/)

May come in handy later:

 * it might be useful to collect data from Openshift instances as well, so I collected some input on this front:
    * [Prometheus Federation](https://prometheus.io/docs/prometheus/latest/federation/)
    * [Prom 1 -> Prom 2 connection](https://www.robustperception.io/accessing-data-from-prometheus-1-x-in-prometheus-2-0)
    * [Streaming features might be useful to gather data from remote proms](https://prometheus.io/blog/2019/10/10/remote-read-meets-streaming/)
 * [Controlling multi service Systemd environment](https://prometheus.io/docs/prometheus/latest/federation/)
   * the idea is great, have a meta service which will manage the other services for you that belong to a shared application
   * starting worked fine, but stopping not so much
   * dropped for now, will have a look again on a reworking session
