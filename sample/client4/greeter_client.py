from __future__ import print_function
import os
import grpc

from datetime import datetime
from time import sleep
from concurrent import futures


import translator_pb2
import translator_pb2_grpc

def run_stream_trans_req(dest_lang,contents):
    #print(contents)
    for content in contents:
        for line in content:
            yield translator_pb2.Text(value=line,dest=dest_lang)
    
def run_stream_trans(contents):
    stub = translator_pb2_grpc.TranslatorStub(channel)
    s2=os.environ.get("dest")
    responses = stub.StreamTrans(run_stream_trans_req(s2,contents[1:]))
    return responses
    
def run_parallel_with_stream(channel):
    startTime = datetime.now()
    executor = futures.ThreadPoolExecutor(max_workers=200)
    with open("english.txt",'r') as f:
        data=f.readlines()
        responses=list(executor.map(run_stream_trans,[[channel,data[i:i+2]] for i in range(0,len(data),2) ]))
    s2=os.environ.get("dest")
    with open("/etc/data4/"+s2+"_parallel_streams"+".txt",'w') as f:
        for response in responses:
            for rep in response:
                f.write(rep.value)
                if rep.value!='\n':
                    f.write('\n')
        f.close()
    print("parallel streams case :"+str(datetime.now() - startTime))
    

if __name__ == '__main__':
    with open('haproxy.crt', 'rb') as f:
        trusted_certs = f.read()
    credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
    #print(os.environ.get("SERVER_ADDRESS"))
    print("\n calling translator server---- \n")
    channel = grpc.secure_channel(os.environ.get("SERVER_ADDRESS"),credentials)
    run_parallel_with_stream(channel)

