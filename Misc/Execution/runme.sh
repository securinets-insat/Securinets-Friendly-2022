#!/bin/bash

docker build -t eval_jail .
docker run -it -p 1337:1234 eval_jail
