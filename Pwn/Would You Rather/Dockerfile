FROM ubuntu

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd
WORKDIR /home/ctf

COPY flag/flag.txt .
COPY backup/chall .
COPY backup/libc.so.6 .
COPY backup/ld-linux-x86-64.so.2 .
COPY ynetd .

RUN chmod 777 ./ynetd
RUN chown -R ctf:ctf /home/ctf

USER ctf
CMD ./ynetd -p 1234 ./chall 2>/dev/null