DESTDIR :=
PREFIX := /usr/local

.PHONY: default
default: build



.PHONY: install
install: build/pwndocker.tar _install
	sudo docker load --input build/pwndocker.tar

.PHONY: _install
_install:
	install -Dm755 src/pwndocker.py ${DESTDIR}${PREFIX}/bin/pwndocker
	install -Dm755 src/glibc-fetch.py ${DESTDIR}${PREFIX}/bin/glibc-fetch



.PHONY: remove
remove:
	rm ${DESTDIR}${PREFIX}/bin/pwndocker
	rm ${DESTDIR}${PREFIX}/bin/glibc-fetch
	sudo docker image rm pwndocker



.PHONY: build
build: build/pwndocker.tar



build/pwndocker.tar: docker/Dockerfile docker/.dockerignore docker/src/ln-static.c
	sudo docker build --tag pwndocker docker/
	sudo docker save --output=build/pwndocker.tar pwndocker
	sudo chmod 644 build/pwndocker.tar
	sudo docker image rm pwndocker
