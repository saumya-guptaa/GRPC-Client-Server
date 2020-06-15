from __future__ import print_function
import os
import grpc

from datetime import datetime
from time import sleep
from concurrent import futures
import matplotlib.pyplot as plt


import translator_pb2
import translator_pb2_grpc

   
def run_translator(channel):
    stub = translator_pb2_grpc.TranslatorStub(channel)
    s1=os.environ.get("Text")
    s2=os.environ.get("dest")
    text = translator_pb2.Text(value=s1,dest=s2)
    response = stub.GoogTrans(text)
    #print(response.value)
    
        
def run():
    with open('haproxy.crt', 'rb') as f:
        trusted_certs = f.read()
    credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
    #print(os.environ.get("SERVER_ADDRESS"))
    print("\n calling translator server---- \n")
    channel = grpc.secure_channel(os.environ.get("SERVER_ADDRESS"),credentials)
    workers=1
    j=0
    while (workers<=10):
        startTime = datetime.now()
        executor = futures.ThreadPoolExecutor(max_workers=workers)
        future=list(executor.map(run_translator,[channel for i in range(workers)]))
        print("{} :- Number of clients = {} :- time = {} \n".format(j+1,workers,datetime.now() - startTime))
        #print(datetime.now() - startTime)
        workers*=10
        j+=1
        sleep(1)
    '''stub = translator_pb2_grpc.TranslatorStub(channel)
#    s1=input('Enter string here: ')
#    s2=input('Enter dest here: ')
    s1=os.environ.get("Text")
    s2=os.environ.get("dest")
    text = translator_pb2.Text(value=s1,dest=s2)
    response = stub.GoogTrans(text)
    print(response.value)'''

if __name__ == '__main__':
    run()

