FROM ubuntu AS app

FROM pwn.red/jail
COPY --from=app / /srv

RUN mkdir /srv/HackThePlanet/
RUN mkdir /srv/HackThePlanet/flags/

COPY main /srv/app/run
COPY flag.txt /srv/HackThePlanet/flags/flag0x666.txt

ENV JAIL_TIME=60
