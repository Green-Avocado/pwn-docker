DESTDIR :=
PREFIX := /usr/local

.PHONY: default
default: install

.PHONY: install
install: build _install
	sudo docker import pwndocker.tar

.PHONY: _install
_install:
	install -Dm755 ./src/pwndocker.py ${DESTDIR}${PREFIX}/bin/pwndocker
	install -Dm755 ./src/glibc-fetch.py ${DESTDIR}${PREFIX}/bin/glibc-fetch

.PHONY: build
build: pwndocker.tar

.PHONY: remove
remove:
	sudo docker image rm pwndocker
	rm ${DESTDIR}${PREFIX}/bin/pwndocker
	rm ${DESTDIR}${PREFIX}/bin/glibc-fetch

pwndocker.tar:
	sudo docker build --tag pwndocker ./docker
	sudo docker save --output=pwndocker.tar pwndocker
	sudo chmod 644 pwndocker.tar
	sudo docker image rm pwndocker
