# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import translator_pb2 as translator__pb2


class TranslatorStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GoogTrans = channel.unary_unary(
                '/Translator/GoogTrans',
                request_serializer=translator__pb2.Text.SerializeToString,
                response_deserializer=translator__pb2.returntext.FromString,
                )


class TranslatorServicer(object):
    """Missing associated documentation comment in .proto file"""

    def GoogTrans(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TranslatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GoogTrans': grpc.unary_unary_rpc_method_handler(
                    servicer.GoogTrans,
                    request_deserializer=translator__pb2.Text.FromString,
                    response_serializer=translator__pb2.returntext.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Translator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Translator(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def GoogTrans(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Translator/GoogTrans',
            translator__pb2.Text.SerializeToString,
            translator__pb2.returntext.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)