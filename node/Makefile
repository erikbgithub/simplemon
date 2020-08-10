.PHONY: install
install:
	./install_node_exporter.sh
	mkdir -p ~/.config/systemd/user
	cp simple-node-exporter.service ~/.config/systemd/user/
	systemctl --user daemon-reload
