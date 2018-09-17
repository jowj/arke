# python monitoring client
arke is a dumb python monitoring client i am currently working on to monitor http status and docker container runtime.

### http status:
- monitor znc server http status
- monitor pleroma server http status

### docker runtime:
- slackbot

## structure
- runtime file
- vars file that points the client at my servers

## TODO
actually implement the following:
- logging https://docs.python.org/2/library/logging.html - use this to dump data instead of doing my own stupid write function.
    - https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/ this is also probably worth reading
- figure out how to remotely monitor processes from the monitoring host
- figure out how to send data over to my mojo slack bot