DESTDIR ?= ~/bin

.PHONY: default
default: install

.PHONY: install
install: pre_install install

.PHONY: _install
_install:
	install -Dm755 ./src/pwndocker.py ${DESTDIR}/pwndocker
	install -Dm755 ./src/glibc-fetch.py ${DESTDIR}/glibc-fetch

.PHONY: pre_install
pre_install: build_image

.PHONY: remove
remove: remove_image

.PHONY: build_image
build_image:
	sudo docker build -t pwndocker ./docker

.PHONY: remove_image
remove_image:
	sudo docker image rm pwndocker
