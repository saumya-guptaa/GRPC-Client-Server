import grpc
from concurrent import futures
import time

#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

import translator_pb2
import translator_pb2_grpc
from googletrans import Translator

translator = Translator()

class TranslatorServicer(translator_pb2_grpc.TranslatorServicer):

    def GoogTrans(self, request, context):
        response =translator_pb2.Text()
        response.value = str(translator.translate(request.value,dest=request.dest))
        print(response)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))


translator_pb2_grpc.add_TranslatorServicer_to_server(
        TranslatorServicer(), server)

# listen on port 8000
with open('server.key', 'rb') as f:
    private_key = f.read()
with open('server.crt', 'rb') as f:
    certificate_chain = f.read()
server_credentials = grpc.ssl_server_credentials( ( (private_key, certificate_chain), ) )
server.add_secure_port('[::]:50053',server_credentials)
server.start()
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
