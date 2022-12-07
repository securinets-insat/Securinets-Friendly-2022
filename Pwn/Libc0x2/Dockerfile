FROM ubuntu AS app

FROM pwn.red/jail
COPY --from=app / /srv

COPY lib2 /srv/app/run
COPY flag.txt /srv/app/flag.txt
