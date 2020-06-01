from concurrent import futures
import time
import math
import logging

import grpc

import log_pb2
import log_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = log_pb2_grpc.log_sharingStub(channel)
        name=log_pb2.filename(name="sample.log")
        contents=stub.Get_file(name)
        with open ("result.log",'w') as f:
            for content in contents:
                f.write(content.data)
            f.close

if __name__ == '__main__':
    logging.basicConfig()
    run()
