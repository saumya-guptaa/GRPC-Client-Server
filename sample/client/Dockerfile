FROM ubuntu:bionic
RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install grpcio
FROM grpc/python:1.4
RUN pip3 install googletrans
#RUN apt-get install python3-matplotlib -y
RUN pip3 install matplotlib
# PYTHONIOENCODING = utf8
RUN apt-get update && apt-get install -y locales && locale-gen en_US.UTF-8
# RUN locale-gen en_US.UTF-8
# ENV LANG en_US.UTF-8
# ENV LANGUAGE en_US:en
# ENV LC_ALL en_US.UTF-8
ENV LANG C.UTF-8
USER root



WORKDIR /source/greeter
COPY . .

ENTRYPOINT ["/source/greeter/start_service.sh"]

