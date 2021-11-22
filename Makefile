DESTDIR ?= ~/bin

.PHONY: pre_install
pre_install: build_image

.PHONY: install
install:
	install -Dm755 ./src/pwndocker.py ${DESTDIR}/pwndocker
	install -Dm755 ./src/glibc-fetch.py ${DESTDIR}/glibc-fetch

.PHONY: pre_remove
pre_remove: remove_image

.PHONY: build_image:
build_image: docker/ln-static
	sudo docker build -t pwndocker ./docker

.PHONY: remove_image:
remove_image:
	sudo docker image rm pwndocker

docker/ln-static: src/ln-static.c
	gcc src/ln-static.c -o docker/ln-static --static
