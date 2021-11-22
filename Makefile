DESTDIR :=
PREFIX := /usr/local

.PHONY: default
default: install

.PHONY: install
install: build install_image
	install -Dm755 ./src/pwndocker.py ${DESTDIR}${PREFIX}/pwndocker
	install -Dm755 ./src/glibc-fetch.py ${DESTDIR}${PREFIX}/glibc-fetch

.PHONY: build
build: build_image

.PHONY: remove
remove: remove_image

.PHONY: build_image
build_image: pwndocker.tar

.PHONY: install_image
install_image: build_image
	docker import pwndocker.tar

.PHONY: remove_image
remove_image:
	sudo docker image rm pwndocker

pwndocker.tar:
	sudo docker build --tag pwndocker ./docker
	sudo docker export --output=pwndocker.tar pwndocker
	docker image rm --filter label=stage=builder
