build:
	podman build -t simpleprom .

install:
	cp simpleprom.service /etc/systemd/system/simpleprom.service
	systemctl daemon-reload

all: build install
