import grpc
from concurrent import futures
import time
import os

import translator_pb2
import translator_pb2_grpc
# from googletrans import Translator
from google.cloud import translate_v2 as translate

translate_client = translate.Client()


class TranslatorServicer(translator_pb2_grpc.TranslatorServicer):
    def GoogTrans(self, request, context):
        response =translator_pb2.returntext()
        # print('Waiting for Operation to Complete...')
        if request.value=='\n': 
            return translator_pb2.returntext(value=request.value)
        else :
            result=translate_client.translate(request.value,target_language=request.dest)
            response.value = str(result['translatedText'])
            return response
        
    def StreamTrans(self, request_iterator, context):
        for line in request_iterator:
            if line.value=='\n':
                yield translator_pb2.returntext(value=line.value)
            else:
                result = translate_client.translate(line.value,target_language=line.dest)
                yield translator_pb2.returntext(value=str(result['translatedText']))


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))


translator_pb2_grpc.add_TranslatorServicer_to_server(
        TranslatorServicer(), server)

# listen on port 8000
with open('example.key', 'rb') as f:
    private_key = f.read()
with open('example.crt', 'rb') as f:
    certificate_chain = f.read()
server_credentials = grpc.ssl_server_credentials( ( (private_key, certificate_chain), ) )
server.add_secure_port('[::]:50054',server_credentials)
server.start()
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
