FROM ubuntu
RUN apt-get upgrade
RUN apt-get update
RUN apt-get -y install python3

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd
WORKDIR /home/ctf

COPY jail.py .
COPY flag.txt .
COPY ynetd .
RUN chmod 777 ./ynetd

RUN chown -R ctf:ctf /home/ctf
USER ctf
CMD ./ynetd -p 1234 "python3 jail.py" 2>/dev/null
