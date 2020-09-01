SLACK_URL := TODO set SLACK_URL variable!

.PHONY: install run
install:
	mkdir -p /tmp/simplealmandata
	mkdir -p ~/.config/systemd/user
	cp simplealman.service ~/.config/systemd/user
	systemctl --user daemon-reload
	mkdir -p /tmp/workaround
	cp simplealman.yaml /tmp/workaround
	podman run --rm -i -v /tmp/workaround:/workdir:Z mikefarah/yq:latest yq write --inplace --style single simplealman.yaml global.slack_api_url "$(SLACK_URL)"
	cp /tmp/workaround/simplealman.yaml /usr/tmp

run:
	systemctl --user restart simplealman
	sleep 2
	systemctl --user status simplealman --no-pager
