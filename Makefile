SLACK_URL := TODO set SLACK_URL variable!


.PHONY: install run
install:
	make install -C node
	make install -C prom
	make install -C graf
	make install -C alman SLACK_URL=$(SLACK_URL)

run:
	make run -C node
	systemctl --user restart simplegraf
	systemctl --user status simplegraf --no-pager
	make run -C prom
	make run -C alman
	podman ps

all: install run
