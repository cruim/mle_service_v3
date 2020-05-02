# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import mle_service_pb2 as mle__service__pb2


class MleServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_predict = channel.unary_unary(
                '/MleService/get_predict',
                request_serializer=mle__service__pb2.Request.SerializeToString,
                response_deserializer=mle__service__pb2.Responce.FromString,
                )


class MleServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def get_predict(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MleServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_predict': grpc.unary_unary_rpc_method_handler(
                    servicer.get_predict,
                    request_deserializer=mle__service__pb2.Request.FromString,
                    response_serializer=mle__service__pb2.Responce.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MleService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MleService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def get_predict(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MleService/get_predict',
            mle__service__pb2.Request.SerializeToString,
            mle__service__pb2.Responce.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
