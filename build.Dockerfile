# syntax=docker/dockerfile:1

FROM archlinux:base-devel

COPY PKGBUILD/* /tmp/

ENV PKGDEST=/mnt
CMD ["makepkg", "-s"]
