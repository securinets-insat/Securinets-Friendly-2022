
#!/bin/bash

docker build -t warmup_jail .
docker run -it -p 1337:2022 warmup_jail
