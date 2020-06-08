FROM ubuntu:bionic
RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install grpcio
FROM grpc/python:1.4
RUN pip3 install googletrans
#RUN apt-get install python3-matplotlib -y
#RUN python3 --version
RUN pip3 install matplotlib
#RUN apt-get install tk-dev 
#RUN apt-get install python3-tk


WORKDIR /source/greeter
COPY . .

ENTRYPOINT ["/source/greeter/start_service.sh"]

