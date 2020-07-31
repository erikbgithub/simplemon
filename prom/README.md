## Simple Prometheus Monitoring DB

This setup will install prometheus for you in a way that you can easily track
local services with it. As default it is integrated with the
[simpleserver](https://github.com/rhdojun/simpleserver) example developed by
yours truly and both can be used together as a template for self hosted web
services.

Interesting projects and blog posts used in the production of this example.
Maybe later I go into explaining what I used from which. Feel free to give
me a ping if I haven't updated this at the time of your reading:
 - https://github.com/Lusitaniae/apache_exporter
 - https://www.tecmint.com/monitor-apache-web-server-load-and-page-statistics/
 - https://techbeacon.com/enterprise-it/monitoring-demystified-guide-logging-tracing-metrics

## Howto

```
$ sudo make build
$ sudo make install
$ sudo systemctl restart simpleprom
$ sudo systemctl status simpleprom
# hopefully something green
```

Then go to your browser and check out http://localhost:9090/targets .
