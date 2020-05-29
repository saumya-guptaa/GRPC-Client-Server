from concurrent import futures
import time
import math
import logging

import grpc

import total_pb2
import total_pb2_grpc
import service_guide_resources

def get_service(service_db, name):
    for service_add in service_db:
        if service_add.name == name.name :
            return service_add
    return None


class serviceguideServicer(total_pb2_grpc.serviceguideServicer):

    def __init__(self):
        self.db = service_guide_resources.read_service_guide_database()

    def Getservice(self, request, context):
        service_add = get_service(self.db, request)
        if service_add is None:
            return total_pb2.service_add(address="", port="")
        else:
            return service_add



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    total_pb2_grpc.add_serviceguideServicer_to_server(
        serviceguideServicer(), server)
    server.add_insecure_port('[::]:50050')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
