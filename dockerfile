FROM alpine:3.7
LABEL maintainer "me@jowj.net"

RUN apk update

RUN apk add \
    python3 \ 
    python-dev

RUN python3 -m pip install --upgrade pip \
    && pip3 install requests

COPY ./ ./

CMD python3 ./arke.py