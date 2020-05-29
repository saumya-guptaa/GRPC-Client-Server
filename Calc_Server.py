from concurrent import futures
import time

import grpc

import total_pb2
import total_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Calculator(total_pb2_grpc.CalculatorServicer):

  def Add(self, request, context):
    return total_pb2.AddReply(n1=request.n1+request.n2)

  def Substract(self, request, context):
    return total_pb2.SubstractReply(n1=request.n1-request.n2)

  def Multiply(self, request, context):
    return total_pb2.MultiplyReply(n1=request.n1*request.n2)

  def Divide(self, request, context):
    return total_pb2.DivideReply(f1=request.n1/request.n2)


def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  total_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
  print('Starting server. Listening on port 50050.')
  server.add_insecure_port('[::]:50052')
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()
