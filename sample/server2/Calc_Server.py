from concurrent import futures
import time
import os

import grpc

import Calc_pb2
import Calc_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Calculator(Calc_pb2_grpc.CalculatorServicer):

  def Add(self, request, context):
    return Calc_pb2.AddReply(n1=request.n1+request.n2)

  def Substract(self, request, context):
    return Calc_pb2.SubstractReply(n1=request.n1-request.n2)

  def Multiply(self, request, context):
    return Calc_pb2.MultiplyReply(n1=request.n1*request.n2)

  def Divide(self, request, context):
    return Calc_pb2.DivideReply(f1=request.n1/request.n2)


def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  Calc_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
  with open('server.key', 'rb') as f:
    private_key = f.read()
  with open('server.crt', 'rb') as f:
    certificate_chain = f.read()
  server_credentials = grpc.ssl_server_credentials( ( (private_key, certificate_chain), ) )
  server.add_secure_port('[::]:'+os.environ.get("port"),server_credentials)
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()
