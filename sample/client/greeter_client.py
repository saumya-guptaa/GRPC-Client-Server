from __future__ import print_function
import os
import grpc

from datetime import datetime
from time import sleep
from concurrent import futures
import matplotlib.pyplot as plt

import helloworld_pb2
import helloworld_pb2_grpc

import Calc_pb2
import Calc_pb2_grpc

import translator_pb2
import translator_pb2_grpc

import log_pb2
import log_pb2_grpc



def run():
    with open('haproxy.crt', 'rb') as f:
        trusted_certs = f.read()
    credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
    print("\n calling default server---- \n")
    channel = grpc.secure_channel(os.environ.get("SERVER_ADDRESS"),credentials)
    count=0
    with open("/etc/data1/"+"result"+".txt",'w+') as f:
        f.write("Greeter Client Server Output----\n"+"\n")
        for _ in range(10):
            stub = helloworld_pb2_grpc.GreeterStub(channel)
            response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
            count=count+1
            f.write("Greeter Client Received: "+response.message + str(count)+"\n")
    f.close()
        
def run1():
    with open('haproxy.crt', 'rb') as f:
        trusted_certs = f.read()
    credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
    print("\n calling calculator server---- \n")
    channel = grpc.secure_channel(os.environ.get("SERVER_ADDRESS"),credentials)
    stub = Calc_pb2_grpc.CalculatorStub(channel)
    a=os.environ.get("Enter_Number1_here")
    b=os.environ.get("Enter_Number2_here")
    with open("/etc/data1/"+"result"+".txt",'a+') as f:
        f.write("\nCalculator server Output---- \n")
        f.write("Number_1 ={}  Number_2={}".format(a,b)+"\n")
    f.close()
    p=int(a)
    q=int(b)
    with open("/etc/data1/"+"result"+".txt",'a+') as f:
        response = stub.Add(Calc_pb2.AddRequest(n1=p,n2=q))
        f.write("Addition result : {}".format(response.n1)+"\n")
        response = stub.Substract(Calc_pb2.SubstractRequest(n1=p,n2=q))
        f.write("Subtraction result : {}".format(response.n1)+"\n")
        response = stub.Multiply(Calc_pb2.MultiplyRequest(n1=p,n2=q))
        f.write("Multiplication result : {}".format(response.n1)+"\n")
        response = stub.Divide(Calc_pb2.DivideRequest(n1=p,n2=q))
        f.write("Division result : {}".format(response.f1)+"\n")
    f.close()
        
def run2():
    with open('haproxy.crt', 'rb') as f:
        trusted_certs = f.read()
    credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
    print("\n calling translator server---- \n")
    channel = grpc.secure_channel(os.environ.get("SERVER_ADDRESS"),credentials)
    stub = translator_pb2_grpc.TranslatorStub(channel)
    s1=os.environ.get("Text")
    s2=os.environ.get("dest")
    text = translator_pb2.Text(value=s1,dest=s2)
    response = stub.GoogTrans(text)
    with open("/etc/data1/"+"result"+".txt",'a+') as f:
        f.write("\nTranslator Server Output----\n")
        f.write("String given by Client to translate: "+ s1 + "\nDestined Langauge: "+ s2)
        f.write("\nTranslated String: "+response.value+"\n")
    f.close()

def run3():
    with open('haproxy.crt', 'rb') as f:
        trusted_certs = f.read()
    credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
    print("\n calling log server---- \n")
    channel = grpc.secure_channel(os.environ.get("SERVER_ADDRESS"),credentials)
    stub = log_pb2_grpc.log_sharingStub(channel)
    file_name=os.environ.get("log_file")
    name=log_pb2.filename(name=file_name)
    contents=stub.Get_file(name)
    with open ("/etc/data1/"+"result"+".txt",'a+') as f:
        f.write("\nLog Server Output----\n")
        for content in contents:
            f.write(content.data)
    f.close

if __name__ == '__main__':
    run()
    run1()
    run2()
    run3()

