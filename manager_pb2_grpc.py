# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import manager_pb2 as manager__pb2


class CollectionManagerStub(object):
    """CollectionManager is an endpoint that can retrieve and publish Collection
    contents for clients.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PublishContent = channel.unary_unary(
                '/manager.CollectionManager/PublishContent',
                request_serializer=manager__pb2.Publish.Request.SerializeToString,
                response_deserializer=manager__pb2.Publish.Response.FromString,
                )
        self.RetrieveContent = channel.unary_unary(
                '/manager.CollectionManager/RetrieveContent',
                request_serializer=manager__pb2.Retrieve.Request.SerializeToString,
                response_deserializer=manager__pb2.Retrieve.Response.FromString,
                )


class CollectionManagerServicer(object):
    """CollectionManager is an endpoint that can retrieve and publish Collection
    contents for clients.
    """

    def PublishContent(self, request, context):
        """PublishContent publishes content based on the request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetrieveContent(self, request, context):
        """RetrieveContent retrieves content based on the request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CollectionManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PublishContent': grpc.unary_unary_rpc_method_handler(
                    servicer.PublishContent,
                    request_deserializer=manager__pb2.Publish.Request.FromString,
                    response_serializer=manager__pb2.Publish.Response.SerializeToString,
            ),
            'RetrieveContent': grpc.unary_unary_rpc_method_handler(
                    servicer.RetrieveContent,
                    request_deserializer=manager__pb2.Retrieve.Request.FromString,
                    response_serializer=manager__pb2.Retrieve.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'manager.CollectionManager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CollectionManager(object):
    """CollectionManager is an endpoint that can retrieve and publish Collection
    contents for clients.
    """

    @staticmethod
    def PublishContent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/manager.CollectionManager/PublishContent',
            manager__pb2.Publish.Request.SerializeToString,
            manager__pb2.Publish.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RetrieveContent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/manager.CollectionManager/RetrieveContent',
            manager__pb2.Retrieve.Request.SerializeToString,
            manager__pb2.Retrieve.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
