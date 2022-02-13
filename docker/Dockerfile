# syntax=docker/dockerfile:1

FROM debian:8.10-slim as build-env
LABEL build=pwndocker

RUN apt-get update && apt-get install -y \
    gcc

RUN mkdir /build/

COPY ln-static.c /src/

RUN gcc /src/ln-static.c --static -o /build/ln-static



FROM debian:8.10-slim

RUN dpkg --add-architecture i386
RUN apt-get update && apt-get install -y \
    gdbserver \
    htop \
    libc6:i386 \
    ltrace \
    strace \
    socat

COPY --from=build-env /build/ln-static /tmp/
COPY entrypoint.sh /tmp/

WORKDIR /mnt/

EXPOSE 1337 13337

ENTRYPOINT ["/tmp/entrypoint.sh"]
