FROM php:fpm-alpine

# Install a few dependencies here...

COPY ./ /var/www/html

COPY ./flag.txt /
WORKDIR /
RUN chmod 444 ./flag.txt


RUN addgroup --gid 1000 ctf
RUN adduser --system --no-create-home --disabled-password --uid 1000 --ingroup ctf firecrackers

RUN chown -R firecrackers:ctf /var/www

USER firecrackers
