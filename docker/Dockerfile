FROM debian:8.10-slim

RUN dpkg --add-architecture i386
RUN apt-get update && apt-get install -y \
    gdbserver \
    libc6:i386 \
    ltrace \
    strace \
    socat
COPY ln-static /tmp
WORKDIR /mnt

