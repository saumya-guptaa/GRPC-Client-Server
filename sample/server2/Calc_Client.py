from __future__ import print_function

import grpc

import Calc_pb2
import Calc_pb2_grpc

def run():
  channel = grpc.insecure_channel('localhost:50050')
  stub = Calc_pb2_grpc.CalculatorStub(channel)
  p=input('Enter Number1 here: ')
  q=input('Enter Number2 here: ')
  q=int(q)
  p=int(p)
  response = stub.Add(Calc_pb2.AddRequest(n1=p,n2=q))
  print(response.n1)
  response = stub.Substract(Calc_pb2.SubstractRequest(n1=p,n2=q))
  print(response.n1)
  response = stub.Multiply(Calc_pb2.MultiplyRequest(n1=p,n2=q))
  print(response.n1)
  response = stub.Divide(Calc_pb2.DivideRequest(n1=p,n2=q))
  print(response.f1)

if __name__ == '__main__':
  run()
