from __future__ import print_function
import os
import grpc

from datetime import datetime
from time import sleep
from concurrent import futures


import translator_pb2
import translator_pb2_grpc

   
def text_to_trans(dest_lang):
    with open("english.txt",'r') as f:
        data=f.readlines()
        #print(data)
        for line in data:
            yield translator_pb2.Text(value=line,dest=dest_lang)
        f.close()
        
def run_stream_only(channel):
    startTime = datetime.now()
    stub = translator_pb2_grpc.TranslatorStub(channel)
    s2=os.environ.get("dest")
    responses = stub.StreamTrans(text_to_trans(s2))
    with open("/etc/data3/"+s2+"_stream_only"+".txt",'w') as f:
        for response in responses:
            f.write(response.value)
            if response.value!='\n':
                f.write('\n')
        f.close()
    print("stream only case :"+str(datetime.now() - startTime))
        
def run_translator(content):
    stub = translator_pb2_grpc.TranslatorStub(content[0])
    s2=os.environ.get("dest")
    Text = translator_pb2.Text(value=content[1],dest=s2)
    response = stub.GoogTrans(Text)
    return response.value
        
def run_parallel_only(channel):
    startTime = datetime.now()
    executor = futures.ThreadPoolExecutor(max_workers=300)
    with open("english.txt",'r') as f:
        data=f.readlines()
        responses=list(executor.map(run_translator,[[channel,line] for line in data]))
    s2=os.environ.get("dest")
    with open("/etc/data3/"+s2+"_parallel_only"+".txt",'w') as f:
        for response in responses:
            f.write(response)
            if response!='\n':
                f.write('\n')
        f.close()
    print("parallel only case :"+str(datetime.now() - startTime))
    
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
    executor = futures.ThreadPoolExecutor(max_workers=1000)
    with open("english.txt",'r') as f:
        data=f.readlines()
        responses=list(executor.map(run_stream_trans,[[channel,data[i:i+4]] for i in range(0,len(data),4) ]))
    s2=os.environ.get("dest")
    with open("/etc/data3/"+s2+"_parallel_streams"+".txt",'w') as f:
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
    #run_stream_only(channel)
    run_parallel_only(channel)
    #run_parallel_with_stream(channel)

