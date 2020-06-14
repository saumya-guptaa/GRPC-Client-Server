# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import speech_pb2 as speech__pb2


class SpeechTranslatorStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.translate = channel.unary_unary(
                '/SpeechTranslator/translate',
                request_serializer=speech__pb2.audio.SerializeToString,
                response_deserializer=speech__pb2.rtext.FromString,
                )


class SpeechTranslatorServicer(object):
    """Missing associated documentation comment in .proto file"""

    def translate(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SpeechTranslatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'translate': grpc.unary_unary_rpc_method_handler(
                    servicer.translate,
                    request_deserializer=speech__pb2.audio.FromString,
                    response_serializer=speech__pb2.rtext.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SpeechTranslator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SpeechTranslator(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def translate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SpeechTranslator/translate',
            speech__pb2.audio.SerializeToString,
            speech__pb2.rtext.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)