from __future__ import print_function
import os
import grpc

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
    #print(os.environ.get("SERVER_ADDRESS"))
    print("\n calling default server---- \n")
    channel = grpc.secure_channel(os.environ.get("SERVER_ADDRESS"),credentials)
    for _ in range(10):
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
        print("Greeter client received: " + response.message)
        
def run1():
    with open('haproxy.crt', 'rb') as f:
        trusted_certs = f.read()
    credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
    #print(os.environ.get("SERVER_ADDRESS"))
    print("\n calling calculator server---- \n")
    channel = grpc.secure_channel(os.environ.get("SERVER_ADDRESS"),credentials)
    stub = Calc_pb2_grpc.CalculatorStub(channel)
#    p=input('Enter Number1 here: ')
#    q=input('Enter Number2 here: ')
    a=os.environ.get("Enter_Number1_here")
    b=os.environ.get("Enter_Number2_here")
    print("Number_1 ={}  Number_2={}".format(a,b))
    p=int(a)
    q=int(b)
#    p=15
#    q=2
    response = stub.Add(Calc_pb2.AddRequest(n1=p,n2=q))
    print("addition result : {}".format(response.n1))
    response = stub.Substract(Calc_pb2.SubstractRequest(n1=p,n2=q))
    print("subtraction result : {}".format(response.n1))
    response = stub.Multiply(Calc_pb2.MultiplyRequest(n1=p,n2=q))
    print("multiplication result : {}".format(response.n1))
    response = stub.Divide(Calc_pb2.DivideRequest(n1=p,n2=q))
    print("division result : {}".format(response.f1))
        
def run2():
    with open('haproxy.crt', 'rb') as f:
        trusted_certs = f.read()
    credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
    #print(os.environ.get("SERVER_ADDRESS"))
    print("\n calling translator server---- \n")
    channel = grpc.secure_channel(os.environ.get("SERVER_ADDRESS"),credentials)
    stub = translator_pb2_grpc.TranslatorStub(channel)
#    s1=input('Enter string here: ')
#    s2=input('Enter dest here: ')
    s1=os.environ.get("Text")
    s2=os.environ.get("dest")
    text = translator_pb2.Text(value=s1,dest=s2)
    response = stub.GoogTrans(text)
    print(response.value)

def run3():
    with open('haproxy.crt', 'rb') as f:
        trusted_certs = f.read()
    credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
    #print(os.environ.get("SERVER_ADDRESS"))
    print("\n calling log server---- \n")
    channel = grpc.secure_channel(os.environ.get("SERVER_ADDRESS"),credentials)
    stub = log_pb2_grpc.log_sharingStub(channel)
    file_name=os.environ.get("log_file")
    name=log_pb2.filename(name=file_name)
    contents=stub.Get_file(name)
    with open ("result.log",'w') as f:
        for content in contents:
            f.write(content.data)
        f.close
    with open ("result.log",'r') as f:
        print(f.read(500))
        f.close()

if __name__ == '__main__':
    run()
    run1()
    run2()
    run3()

