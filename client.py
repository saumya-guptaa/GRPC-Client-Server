from __future__ import print_function
import logging
import grpc
import total_pb2
import total_pb2_grpc

def run_service_add(service):
  with grpc.insecure_channel("localhost:50050") as channel:
    stub = total_pb2_grpc.serviceguideStub(channel)
    service_add=stub.Getservice(total_pb2.service_name(name=service))
    #print(service_add.address+":"+service_add.port)
    return service_add.address+":"+service_add.port

def run_greeter():
  service_add=run_service_add("helloworld")
  channel = grpc.insecure_channel(service_add)
  stub = total_pb2_grpc.GreeterStub(channel)
  s1=input('Enter name here: ')
  response = stub.SayHello(total_pb2.HelloRequest(name=s1))
  print("Greeter client received: " + response.message)
  response = stub.SayHelloAgain(total_pb2.HelloRequest(name=s1))
  print("Greeter client received: " + response.message)
  
def run_calc():
  service_add=run_service_add("calculator")
  channel = grpc.insecure_channel(service_add)
  stub = total_pb2_grpc.CalculatorStub(channel)
  p=input('Enter Number1 here: ')
  q=input('Enter Number2 here: ')
  q=int(q)
  p=int(p)
  response = stub.Add(total_pb2.AddRequest(n1=p,n2=q))
  print(response.n1)
  response = stub.Substract(total_pb2.SubstractRequest(n1=p,n2=q))
  print(response.n1)
  response = stub.Multiply(total_pb2.MultiplyRequest(n1=p,n2=q))
  print(response.n1)
  response = stub.Divide(total_pb2.DivideRequest(n1=p,n2=q))
  print(response.f1)
  
def run_translator():
  service_add=run_service_add("translator")
  channel = grpc.insecure_channel(service_add)
  stub = total_pb2_grpc.TranslatorStub(channel)
  s1=input('Enter string here: ')
  s2=input('Enter dest here: ')
  text = total_pb2.Text(value=s1,dest=s2)
  response = stub.GoogTrans(text)
  print(response.value)

if __name__ == '__main__':
  logging.basicConfig()
  run_greeter()
  run_calc()
  run_translator()
