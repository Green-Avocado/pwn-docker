# syntax=docker/dockerfile:1

FROM debian:8.10-slim

RUN dpkg --add-architecture i386
RUN apt-get update && apt-get install -y \
    gdbserver \
    htop \
    libc6:i386 \
    ltrace \
    strace \
    socat

COPY entrypoint.sh /tmp/

WORKDIR /mnt/

EXPOSE 1337 13337

ENTRYPOINT ["/tmp/entrypoint.sh"]
