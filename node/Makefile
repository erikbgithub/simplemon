.PHONY: install run
install:
	./install_node_exporter.sh
	mkdir -p ~/.config/systemd/user
	cp simple-node-exporter.service ~/.config/systemd/user/
	systemctl --user daemon-reload

run:
	systemctl --user restart simple-node-exporter
	sleep 2
	systemctl --user status simple-node-exporter --no-pager
