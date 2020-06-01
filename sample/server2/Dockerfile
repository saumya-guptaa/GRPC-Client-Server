FROM ubuntu:bionic
RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install grpcio
FROM grpc/python:1.4


WORKDIR /source/calc
COPY . .

ENTRYPOINT ["/source/calc/start_service.sh"]

