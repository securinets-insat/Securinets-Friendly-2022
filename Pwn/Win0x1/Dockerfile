FROM ubuntu AS app

RUN apt-get upgrade
RUN apt-get update

RUN dpkg --add-architecture i386 && \
    apt-get -y update && \
    apt install -y \
    libc6:i386 \
    libc6-dbg:i386 \
    libc6-dbg \
    lib32stdc++6 \
    g++-multilib

FROM pwn.red/jail
COPY --from=app / /srv

COPY win1 /srv/app/run
COPY flag.txt /srv/app/flag.txt
