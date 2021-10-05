FROM ubuntu:18.04
RUN apt update && apt install -y xinetd iproute2 && rm -rf /var/lib/apt/lists/*
RUN useradd pwrld
RUN mkdir /home/pwrld
RUN mkdir /home/pwrld/pwn
COPY ./pwn.xinetd /etc/xinetd.d/pwn
COPY ./start.sh /start.sh
COPY ./setup.sh /setup.sh
COPY ./challenge /home/pwrld/pwn/baby_heap/challenge
RUN chown -R root:pwrld /home/pwrld/pwn && chmod -R 750 /home/pwrld/pwn
RUN chmod +x /setup.sh
RUN chown root:pwrld /start.sh && chmod 750 /start.sh
CMD ["/setup.sh"]

EXPOSE 8888