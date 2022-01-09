DESTDIR := /usr/local

.PHONY: default
default: build



.PHONY: install
install: pwndocker.tar _install
	sudo docker load --input pwndocker.tar

.PHONY: _install
_install:
	install -Dm755 src/pwndocker.py ${DESTDIR}/bin/pwndocker
	install -Dm755 src/glibc-fetch.py ${DESTDIR}/bin/glibc-fetch



.PHONY: remove
remove:
	rm ${DESTDIR}/bin/pwndocker
	rm ${DESTDIR}/bin/glibc-fetch
	sudo docker image rm pwndocker



.PHONY: build
build: pwndocker.tar



pwndocker.tar: docker/Dockerfile docker/.dockerignore docker/src/ln-static.c
	sudo docker build --tag pwndocker docker/
	sudo docker save --output=pwndocker.tar pwndocker
	sudo chmod 644 pwndocker.tar
	sudo docker image rm pwndocker
