FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y --no-install-recommends python3=3.6.7-1~18.04 \
                                               python3-pip=9.0.1-2.3~ubuntu1.18.04.1 \
                                               python3-setuptools=39.0.1-2 \
                                               tcpdump=4.9.2-3 && \
    pip3 install wheel==0.33.6 && \
    pip3 install flask==1.1.1 scapy==2.4.3 && \
    mkdir /opt/highsaltlevels/

COPY app/ /opt/highsaltlevels/app/
COPY lib/ /opt/highsaltlevels/lib/
COPY etc/ /opt/highsaltlevels/etc/

ENV PYTHONPATH="${PYTHONPATH}:/opt/highsaltlevels/lib/"

EXPOSE 7777

WORKDIR /opt/highsaltlevels/app/

CMD ./app.py
