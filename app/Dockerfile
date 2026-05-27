FROM alpine:3.23.4

RUN apk add --update --no-cache python3 curl iptables

WORKDIR /opt/
USER 1000:1000
EXPOSE 8080

COPY app.py ./

CMD ["/usr/bin/python3", "/opt/app.py"]