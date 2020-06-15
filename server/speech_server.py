import grpc
from concurrent import futures
import time
import os

import translator_pb2
import translator_pb2_grpc
import io
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums

client = speech_v1.SpeechClient()




class SpeechTranslatorServicer(translator_pb2_grpc.SpeechTranslatorServicer):
    def translate(self, request, context):
        # print(request.path)
        res=translator_pb2.rtext()
        # print(request.)
        language_code = "en-US"
        sample_rate_hertz = 16000
        encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16
        config = {
            "language_code": language_code,
            "sample_rate_hertz": sample_rate_hertz,
            "encoding": encoding,
        }
        local_file_path = "/home/yash/intern/GRPC-Client-Server/client/"+request.path
        with io.open(local_file_path, "rb") as f:
            content = f.read()
        audio = {"content": content}

        operation = client.long_running_recognize(config, audio)

        print(u"Waiting for operation to complete...")
        response = operation.result()
        s1=""
        for result in response.results:
            alternative = result.alternatives[0]
            s1=alternative.transcript
        # print(s1)
        # print("hey")
        res.value=str(s1)
        # print(res.value)
        return res

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))
    translator_pb2_grpc.add_SpeechTranslatorServicer_to_server(SpeechTranslatorServicer(), server)
    with open('example.key', 'rb') as f:
    	private_key = f.read()
    with open('example.crt', 'rb') as f:
    	certificate_chain = f.read()
    server_credentials = grpc.ssl_server_credentials( ( (private_key, certificate_chain), ) )
    server.add_secure_port('[::]:50051',server_credentials)
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
