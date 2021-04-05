FROM debian:8.10-slim

RUN apt-get update
RUN apt-get install -y socat gdbserver ltrace strace
COPY ln-static /tmp
WORKDIR /mnt

