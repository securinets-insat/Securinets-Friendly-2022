FROM ubuntu:18.04

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd
WORKDIR /home/ctf

COPY flag/flag.txt .
COPY attachments/lock .
COPY ynetd .

RUN chmod 777 ./ynetd
RUN chown -R ctf:ctf /home/ctf

USER ctf
CMD ./ynetd -p 1234 ./lock 2>/dev/null