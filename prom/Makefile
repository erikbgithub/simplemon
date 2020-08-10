.PHONY: install
install:
	mkdir -p ~/.config/systemd/user
	cp simpleprom.service ~/.config/systemd/user/
	systemctl --user daemon-reload
	cp simpleprom.yaml /usr/tmp/simpleprom.yaml
