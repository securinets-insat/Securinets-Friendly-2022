FROM ubuntu
RUN apt-get upgrade
RUN apt-get update

RUN useradd -d /home/jailed/ -m -p jailed -s /bin/bash jailed
RUN echo "jailed:jailed" | chpasswd
WORKDIR /home/jailed

COPY a.out .
COPY ynetd .
RUN chmod 777 ./ynetd

RUN chown -R jailed:jailed /home/jailed
USER jailed
CMD ./ynetd -p 2022 "./a.out"
