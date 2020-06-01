from concurrent import futures
import time
import math
import logging

import grpc

import log_pb2
import log_pb2_grpc

class log_sharingServicer(log_pb2_grpc.log_sharingServicer):
    def Get_file(self, request, context):
        with open(request.name,'r') as f:
            dat=f.readlines()
            for line in dat:
                yield log_pb2.content(data=line)
            f.close()
                

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    log_pb2_grpc.add_log_sharingServicer_to_server(
    	log_sharingServicer(), server)
    with open('server.key', 'rb') as f:
        private_key = f.read()
    with open('server.crt', 'rb') as f:
        certificate_chain = f.read()
    server_credentials = grpc.ssl_server_credentials( ( (private_key, certificate_chain), ) )
    server.add_secure_port('[::]:50054',server_credentials)
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    logging.basicConfig()
    serve()
