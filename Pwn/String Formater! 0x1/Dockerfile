FROM ubuntu AS app

FROM pwn.red/jail
COPY --from=app / /srv

COPY main /srv/app/run

ENV JAIL_ENV_FLAG="Securinets{Env_V4r5_4r3_\$av3d_In_7H3_StaCK!}"
