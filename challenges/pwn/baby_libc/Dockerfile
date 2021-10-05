FROM ubuntu:18.04
LABEL Description="baby_libc" VERSION='1.0'

# RUN apt update
RUN useradd pwrld
RUN mkdir /home/pwrld
RUN mkdir /home/pwrld/pwn
RUN mkdir /home/pwrld/pwn/baby_libc

COPY ./babylibc /home/pwrld/pwn/baby_libc/babylibc
COPY ./flag.txt /home/pwrld/pwn/baby_libc/flag.txt
COPY ./start.sh /home/pwrld/pwn/baby_libc/start.sh
COPY ./ynetd /home/pwrld/pwn/baby_libc/ynetd

RUN chown -R root:pwrld /home/pwrld/pwn/baby_libc && chmod -R 750 /home/pwrld/pwn/baby_libc
RUN chmod +x /home/pwrld/pwn/baby_libc/start.sh
RUN chown root:pwrld /home/pwrld/pwn/baby_libc/start.sh && chmod 750 /home/pwrld/pwn/baby_libc/start.sh

CMD ["/home/pwrld/pwn/baby_libc/setup.sh"]
EXPOSE 4000
