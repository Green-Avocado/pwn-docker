DESTDIR :=
PREFIX := /usr/local

.PHONY: default
default: install

.PHONY: install
install: pwndocker.tar _install
	sudo docker load --input pwndocker.tar

.PHONY: _install
_install:
	install -Dm755 src/pwndocker.py ${DESTDIR}${PREFIX}/bin/pwndocker
	install -Dm755 src/glibc-fetch.py ${DESTDIR}${PREFIX}/bin/glibc-fetch

.PHONY: build
build: pwndocker.tar

.PHONY: remove
remove:
	rm ${DESTDIR}${PREFIX}/bin/pwndocker
	rm ${DESTDIR}${PREFIX}/bin/glibc-fetch
	sudo docker image rm pwndocker

pwndocker.tar: docker/Dockerfile docker/.dockerignore docker/src/ln-static.c
	sudo docker build --tag pwndocker docker/
	sudo docker save --output=pwndocker.tar pwndocker
	sudo chmod 644 pwndocker.tar
	sudo docker image rm pwndocker
