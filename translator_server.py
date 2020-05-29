import grpc
from concurrent import futures
import time

import total_pb2
import total_pb2_grpc
from googletrans import Translator

translator = Translator()

class TranslatorServicer(total_pb2_grpc.TranslatorServicer):

    def GoogTrans(self, request, context):
        response =total_pb2.Text()
        response.value = str(translator.translate(request.value,dest=request.dest))
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))


total_pb2_grpc.add_TranslatorServicer_to_server(
        TranslatorServicer(), server)

# listen on port 8000
print('Starting server. Listening on port 50053.')
server.add_insecure_port('[::]:50053')
server.start()
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
