## Simple Prometheus Monitoring DB

This setup will install prometheus for you in a way that you can easily track
local services with it. As default it is integrated with the
[simpleserver](https://github.com/rhdojun/simpleserver) example developed by
yours truly and both can be used together as a template for self hosted web
services.

## Howto

```
$ make install
$ systemctl --user restart simpleprom
$ systemctl --user status simpleprom
# hopefully something green
```

Then go to your browser and check out `http://localhost:9090/targets`.
