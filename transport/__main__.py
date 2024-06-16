from concurrent import futures

# from loguru import logger
# import math
# import time

import grpc

import transport.protos.transport_pb2_grpc as transport_pb2_grpc
import transport.protos.transport_pb2 as transport_pb2


class TransportServicer(transport_pb2_grpc.TransportServicer):
    """Provides methods that implement functionality of route guide server."""

    def __init__(self):
        pass

    def SendEconomyReport(self, request, context):
        print(request)
        ret = transport_pb2.Confirmaion()

        return ret


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    transport_pb2_grpc.add_TransportServicer_to_server(TransportServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
