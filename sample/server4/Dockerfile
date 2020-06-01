#FROM python:3
#FROM grpc/python
#FROM alpine:3.7

#RUN apk update && apk add python3 bash curl
#RUN python --version
#RUN pip3 install --upgrade pip
#RUN pip3 install googletrans

#RUN python -m venv env

#COPY --from=envoyproxy/envoy /usr/local/bin/envoy /usr/local/bin/envoy

FROM ubuntu:bionic
RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install grpcio
FROM grpc/python:1.4


WORKDIR /source/log
COPY . .

ENTRYPOINT ["/source/log/start_service.sh"]

