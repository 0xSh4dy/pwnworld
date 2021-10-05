FROM ubuntu:18.04
LABEL Description="write-it" VERSION='1.0'

#installation
RUN apt update

#user
RUN adduser --disabled-password --gecos '' pwn 
RUN chown -R root:pwn /home/pwn/
RUN chmod 750 /home/pwn

RUN touch /home/pwn/flag.txt

RUN export TERM=xterm

#Copying file
WORKDIR /home/pwn/
COPY ./challenge/random /home/pwn
COPY ./challenge/flag.txt /home/pwn

#Setting perm..
RUN chown root:pwn /home/pwn/flag.txt
RUN chmod +x /home/pwn/random
RUN chmod 440 /home/pwn/flag.txt
RUN apt-get install socat 

EXPOSE 5002

#Run the program with socat
CMD su pwn -c "/home/pwn/fmt"
