FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y python3=3.6.7-1~18.04 python3-pip=9.0.1-2.3~ubuntu1.18.04.1 && \
    pip3 install flask && \
    mkdir /opt/highsaltlevels/

COPY app/ /opt/highsaltlevels/app/
COPY lib/ /opt/highsaltlevels/lib/
COPY etc/ /opt/highsaltlevels/etc/

EXPOSE 7777

WORKDIR /opt/highsaltlevels/app/

CMD ./app.py
