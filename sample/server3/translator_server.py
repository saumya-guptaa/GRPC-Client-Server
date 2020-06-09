import grpc
from concurrent import futures
import time
import os


# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

import translator_pb2
import translator_pb2_grpc
# from googletrans import Translator
from google.cloud import translate_v2 as translate

# translator = Translator()
translate_client = translate.Client()


class TranslatorServicer(translator_pb2_grpc.TranslatorServicer):
    def GoogTrans(self, request, context):
        response =translator_pb2.Text()
        # s1='你好，世界'
        # s1.decode(encoding='UTF-8',errors='strict')
        # s1=str(s1)
        # s1.encode("utf-8")
        # response.value = s1

        response.value = str(translate_client.translate(request.value,target_language=request.dest))
        # print(response.value)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))


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
