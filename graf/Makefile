.PHONY: install
install:
	mkdir -p ~/.config/systemd/user
	cp simplegraf.service ~/.config/systemd/user/
	systemctl --user daemon-reload
	mkdir -p ~/.local/bin
	cp default-dashboard.py ~/.local/bin
