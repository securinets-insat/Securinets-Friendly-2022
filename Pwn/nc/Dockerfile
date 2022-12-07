FROM ubuntu

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY main .
COPY flag.txt .
COPY ynetd .

USER ctf
CMD ./ynetd -p 1234 ./main