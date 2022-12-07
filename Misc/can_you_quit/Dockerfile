FROM ubuntu AS app

RUN apt-get upgrade
RUN apt-get update

RUN apt-get install vim -y

FROM pwn.red/jail
COPY --from=app / /srv

RUN mkdir /srv/app

COPY run.sh /srv/app/run
COPY hello /srv/app
COPY flag.txt /srv/app

ENV JAIL_TIME=120
