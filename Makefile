DESTDIR := /usr/local

.PHONY: default
default:
	echo "Usage: make install|remove"

.PHONY: install
install:
	install -Dm755 bin/pwndocker.py ${DESTDIR}/bin/pwndocker
	install -Dm755 bin/fetch-libc.py ${DESTDIR}/bin/fetch-libc

.PHONY: remove
remove:
	rm ${DESTDIR}/bin/pwndocker
	rm ${DESTDIR}/bin/fetch-libc
