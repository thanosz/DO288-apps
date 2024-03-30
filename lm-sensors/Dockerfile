FROM alpine:latest
RUN apk update && apk add lm-sensors python3 curl && apk cache clean
ADD httplm.py /
EXPOSE 8080
ENTRYPOINT [ "python3", "/httplm.py" ]

