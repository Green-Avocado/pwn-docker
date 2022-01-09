# syntax=docker/dockerfile:1

FROM archlinux:base-devel

RUN pacman -Syu --noconfirm

RUN echo 'user ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/user
RUN useradd user
USER user:user

WORKDIR /tmp/

COPY PKGBUILD .
COPY pwndocker.install .

ENV PKGDEST=/mnt
CMD ["makepkg", "--syncdeps", "--noconfirm"]
