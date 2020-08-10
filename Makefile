install:
	make install -C node
	make install -C prom
	make install -C graf

run:
	systemctl --user restart simple-node-exporter
	systemctl --user restart simpleprom
	systemctl --user restart simplegraf
	systemctl --user status simple-node-exporter
	systemctl --user status simpleprom
	systemctl --user status simplegraf
	podman ps

all: install run
