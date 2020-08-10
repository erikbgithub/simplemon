#!/usr/bin/python


import requests
import json
import sys

print("This didn't work yet. Grafana first accepts the web requests and then is not able to display the dashboard without a readable error.")
print("TODO: Will dig further later.")
sys.exit(1)


name_simple_prom = "Simple Prom"

response_datasource = requests.post("http://admin:admin@127.0.0.1:3000/api/datasources", json={
     "name": name_simple_prom,
     "type": "prometheus",
     "access": "proxy",
     "url": "http://127.0.0.1:9090",
   })

print(" - Data Source HTTP Status code: ", response_datasource.status_code)
if response_datasource.status_code != 200:
    print(" - Printing Entire Post Response:")
    print(json.dumps(response_datasource.json(), sort_keys=True, indent=2))
    print(" - Done - ")
    sys.exit(1)
else:
    print()

response_dashboard = requests.post("http://admin:admin@127.0.0.1:3000/api/dashboards/db", json={
  "Dashboard": {
    "editable": True,
    "gnetId": None,
    "graphTooltip": 0,
    "id": None,
    "links": [],
    "panels": [
      {
        "aliasColors": {},
        "bars": False,
        "dashLength": 10,
        "dashes": False,
        "datasource": "Simple Prom",
        "fieldConfig": {
          "defaults": {
            "custom": {}
          },
          "overrides": []
        },
        "fill": 1,
        "fillGradient": 0,
        "gridPos": {
          "h": 8,
          "w": 12,
          "x": 7,
          "y": 0
        },
        "hiddenSeries": False,
        "id": None,
        "legend": {
          "avg": False,
          "current": False,
          "max": False,
          "min": False,
          "show": True,
          "total": False,
          "values": False
        },
        "lines": True,
        "linewidth": 1,
        "NonePointMode": "None",
        "percentage": False,
        "pluginVersion": "7.1.3",
        "pointradius": 2,
        "points": False,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": False,
        "steppedLine": False,
        "targets": [
          {
            "expr": "(1 - (node_filesystem_avail_bytes / node_filesystem_size_bytes)) * 100",
            "interval": "",
            "legendFormat": "",
            "refId": "A"
          }
        ],
        "thresholds": [],
        "timeFrom": None,
        "timeRegions": [],
        "timeShift": None,
        "title": "Disk %",
        "tooltip": {
          "shared": True,
          "sort": 0,
          "value_type": "individual"
        },
        "type": "graph",
        "xaxis": {
          "buckets": None,
          "mode": "time",
          "name": None,
          "show": True,
          "values": []
        },
        "yaxes": [
          {
            "format": "short",
            "label": None,
            "logBase": 1,
            "max": None,
            "min": None,
            "show": True
          },
          {
            "format": "short",
            "label": None,
            "logBase": 1,
            "max": None,
            "min": None,
            "show": True
          }
        ],
        "yaxis": {
          "align": False,
          "alignLevel": None
        }
      },
      {
        "datasource": "Simple Prom",
        "fieldConfig": {
          "defaults": {
            "custom": {},
            "mappings": [],
            "thresholds": {
              "mode": "percentage",
              "steps": [
                {
                  "color": "green",
                  "value": None
                },
                {
                  "color": "yellow",
                  "value": 60
                },
                {
                  "color": "red",
                  "value": 80
                }
              ]
            }
          },
          "overrides": []
        },
        "gridPos": {
          "h": 4,
          "w": 7,
          "x": 0,
          "y": 4
        },
        "id": None,
        "options": {
          "colorMode": "value",
          "graphMode": "area",
          "justifyMode": "auto",
          "orientation": "auto",
          "reduceOptions": {
            "calcs": [
              "mean"
            ],
            "fields": "",
            "values": False
          },
          "textMode": "auto"
        },
        "pluginVersion": "7.1.3",
        "targets": [
          {
            "expr": "((node_memory_MemTotal_bytes - node_memory_MemFree_bytes) / node_memory_MemTotal_bytes) * 100",
            "interval": "",
            "legendFormat": "",
            "refId": "A"
          }
        ],
        "timeFrom": None,
        "timeShift": None,
        "title": "Mem %",
        "type": "stat"
      }
    ],
    "schemaVersion": 26,
    "style": "dark",
    "tags": [],
    "templating": {
      "list": []
    },
    "time": {
      "from": "now-6h",
      "to": "now"
    },
    "timepicker": {
      "refresh_intervals": [
        "5s",
        "10s",
        "30s",
        "1m",
        "5m",
        "15m",
        "30m",
        "1h",
        "2h",
        "1d"
      ]
    },
    "timezone": "",
    "title": "node-dashboard",
    "uid": None,
    "version": 2
  }
})

print(" - Dashboard HTTP Status code: ", response_dashboard.status_code)
if response_dashboard.status_code != 200:
    print(" - Printing Entire Post Response:")
    print(json.dumps(response_dashboard.json(), sort_keys=True, indent=2))
    print(" - Done - ")
    sys.exit(2)
