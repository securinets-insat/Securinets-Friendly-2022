FROM ubuntu AS app

FROM pwn.red/jail
COPY --from=app / /srv

COPY lib0 /srv/app/run
COPY flag.txt /srv/app/flag.txt
