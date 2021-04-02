FROM debian:stable-slim

RUN apt-get install -y socat
EXPOSE 1337

