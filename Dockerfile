FROM debian:stable-slim

RUN apt-get update
RUN apt-get install -y socat
COPY ln-static /tmp
WORKDIR /mnt
EXPOSE 1337

