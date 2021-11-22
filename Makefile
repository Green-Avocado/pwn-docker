DESTDIR :=
PREFIX := /usr/local

.PHONY: default
default: install

.PHONY: install
install: build install_image
	install -Dm755 ./src/pwndocker.py ${DESTDIR}${PREFIX}/bin/pwndocker
	install -Dm755 ./src/glibc-fetch.py ${DESTDIR}${PREFIX}/bin/glibc-fetch

.PHONY: build
build: build_image

.PHONY: remove
remove: remove_image

.PHONY: build_image
build_image: pwndocker.tar

.PHONY: install_image
install_image: build_image
	sudo docker import pwndocker.tar

.PHONY: remove_image
remove_image:
	sudo docker image rm pwndocker

pwndocker.tar:
	sudo docker build --tag pwndocker ./docker
	sudo docker save --output=pwndocker.tar pwndocker
	sudo docker image prune --filter label=build=pwndocker
	sudo docker image rm pwndocker
