FROM ubuntu
RUN apt-get upgrade
RUN apt-get update
RUN apt-get -y install python3 python3-pip
RUN pip install pycryptodome

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd
WORKDIR /home/ctf

COPY flag.txt .
COPY server.py .
COPY ynetd .
RUN chmod 777 ./ynetd

RUN chown -R ctf:ctf /home/ctf
USER ctf
CMD ./ynetd -p 1234 "python3 server.py" 2>/dev/null