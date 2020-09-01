.PHONY: install
install:
	mkdir -p ~/.config/systemd/user
	cp simpleprom.service ~/.config/systemd/user/
	systemctl --user daemon-reload
	cp simpleprom.yaml /usr/tmp/simpleprom.yaml
	cp simpleprom.recordings.yaml /usr/tmp/simpleprom.recordings.yaml
	cp simpleprom.alerts.yaml /usr/tmp/simpleprom.alerts.yaml

.PHONY: run
run:
	systemctl --user restart simpleprom
	sleep 2
	systemctl --user status simpleprom --no-pager
