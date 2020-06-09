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
RUN pip install --upgrade pip
RUN pip3 install setuptools --upgrade
RUN pip3 install --upgrade google-cloud-translate
# PYTHONIOENCODING = utf8
RUN apt-get update && apt-get install -y locales && locale-gen en_US.UTF-8
# RUN locale-gen en_US.UTF-8
# ENV LANG en_US.UTF-8
# ENV LANGUAGE en_US:en
# ENV LC_ALL en_US.UTF-8
ENV LANG C.UTF-8
USER root


WORKDIR /source/translator
COPY . .

ENTRYPOINT ["/source/translator/start_service.sh"]

