FROM ubuntu:18.04

# RUN apt-get update

RUN useradd -d /home/pwn/ -m -p ctf -s /bin/bash pwn
RUN echo "pwn:pwn" | chpasswd

WORKDIR /home/pwn

COPY magic .
COPY flag.txt .
COPY ynetd .

RUN chown -R root:root /home/pwn

USER pwn
EXPOSE 4001
CMD ./ynetd -p 4001 ./magic