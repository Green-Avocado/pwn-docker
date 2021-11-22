DESTDIR ?= ~/bin

.PHONY: default
default: install

.PHONY: install
install: build
	install -Dm755 ./src/pwndocker.py ${DESTDIR}/pwndocker
	install -Dm755 ./src/glibc-fetch.py ${DESTDIR}/glibc-fetch

.PHONY: build 
pre_install: build_image

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
	sudo docker build --output type=tar,dest=pwndocker.tar -t pwndocker ./docker
