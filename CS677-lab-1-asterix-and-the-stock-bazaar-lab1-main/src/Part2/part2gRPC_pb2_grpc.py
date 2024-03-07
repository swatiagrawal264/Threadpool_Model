# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import part2gRPC_pb2 as part2gRPC__pb2


class StockTradingStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Lookup = channel.unary_unary(
                '/StockTrading.StockTrading/Lookup',
                request_serializer=part2gRPC__pb2.LookupRequest.SerializeToString,
                response_deserializer=part2gRPC__pb2.LookupResponse.FromString,
                )
        self.Trade = channel.unary_unary(
                '/StockTrading.StockTrading/Trade',
                request_serializer=part2gRPC__pb2.TradeRequest.SerializeToString,
                response_deserializer=part2gRPC__pb2.TradeResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/StockTrading.StockTrading/Update',
                request_serializer=part2gRPC__pb2.UpdateRequest.SerializeToString,
                response_deserializer=part2gRPC__pb2.UpdateResponse.FromString,
                )


class StockTradingServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Lookup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Trade(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StockTradingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Lookup': grpc.unary_unary_rpc_method_handler(
                    servicer.Lookup,
                    request_deserializer=part2gRPC__pb2.LookupRequest.FromString,
                    response_serializer=part2gRPC__pb2.LookupResponse.SerializeToString,
            ),
            'Trade': grpc.unary_unary_rpc_method_handler(
                    servicer.Trade,
                    request_deserializer=part2gRPC__pb2.TradeRequest.FromString,
                    response_serializer=part2gRPC__pb2.TradeResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=part2gRPC__pb2.UpdateRequest.FromString,
                    response_serializer=part2gRPC__pb2.UpdateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'StockTrading.StockTrading', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StockTrading(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Lookup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/StockTrading.StockTrading/Lookup',
            part2gRPC__pb2.LookupRequest.SerializeToString,
            part2gRPC__pb2.LookupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Trade(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/StockTrading.StockTrading/Trade',
            part2gRPC__pb2.TradeRequest.SerializeToString,
            part2gRPC__pb2.TradeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/StockTrading.StockTrading/Update',
            part2gRPC__pb2.UpdateRequest.SerializeToString,
            part2gRPC__pb2.UpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)