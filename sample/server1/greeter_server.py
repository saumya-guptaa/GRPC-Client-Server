# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import os
import time
from time import sleep

import grpc

import helloworld_pb2
import helloworld_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        sleep(0.1)
        return helloworld_pb2.HelloReply(message='Hello, %s from host=%s!' % (request.name, os.environ.get("HOSTNAME", "Unknown")))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
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
