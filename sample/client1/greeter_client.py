from __future__ import print_function
import os
import grpc

from datetime import datetime
from time import sleep
from concurrent import futures
import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import helloworld_pb2
import helloworld_pb2_grpc




def run_greeter(channel):
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
    #print("Greeter client received: " + response.message + str(datetime.now()))

def run():
    with open('haproxy.crt', 'rb') as f:
        trusted_certs = f.read()
    credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
    #print(os.environ.get("SERVER_ADDRESS"))
    print("\n calling default server---- \n")
    channel = grpc.secure_channel(os.environ.get("SERVER_ADDRESS"),credentials)
    workers=1
    j=0
    no_of_workers=[10**(i) for i in range(3)]
    time_taken=[0.0]*3
    while (workers<=100):
        startTime = datetime.now()
        executor = futures.ThreadPoolExecutor(max_workers=workers)
        future=list(executor.map(run_greeter,[channel for i in range(workers)]))
        time_tak=datetime.now() - startTime
        print("{} :- Number of clients = {} :- time = {} \n".format(j+1,workers,time_tak))
        time_taken[j]=(time_tak).total_seconds()*1000
        #print(datetime.now() - startTime)
        workers*=10
        j+=1
        sleep(2)
    
    #print(no_of_workers)
    #print(time_taken)
    plt.plot(no_of_workers, time_taken,linestyle='--',marker='o')  
    plt.xlabel('number of parallel clients')
    plt.ylabel('time taken')
    plt.grid(True)
    plt.title('number of parallel clients vs time taken for server parallel thread=20')
    plt.savefig('/etc/data/result.png') 
    '''count=0
    for _ in range(10):
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
        count=count+1
        print("Greeter client received: " + response.message+str(count))'''
    print("\n")
    #print(future[0].done())
   # sleep(5)
        

if __name__ == '__main__':
    run()

