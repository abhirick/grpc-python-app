import grpc
from concurrent import futures
import time

import welcome_pb2
import welcome_pb2_grpc
from grpc_reflection.v1alpha import reflection

class WelcomeServiceServicer(welcome_pb2_grpc.WelcomeServiceServicer):
    def SayWelcome(self, request, context):
        response = welcome_pb2.WelcomeResponse()
        response.message = f"Welcome, {request.name}!"
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    welcome_pb2_grpc.add_WelcomeServiceServicer_to_server(WelcomeServiceServicer(), server)

    # Enable reflection
    SERVICE_NAMES = (
        welcome_pb2.DESCRIPTOR.services_by_name['WelcomeService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started, listening on port 50051.")
    try:
        while True:
            time.sleep(86400)  # Sleep for a day
    except KeyboardInterrupt:
        print("Shutting down the server...")
        server.stop(0)

if __name__ == '__main__':
    serve()
