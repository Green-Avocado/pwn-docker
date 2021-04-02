FROM debian:stable-slim

RUN apt-get update
RUN apt-get install -y socat
WORKDIR /mnt
EXPOSE 1337

