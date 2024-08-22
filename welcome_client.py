import grpc
import welcome_pb2
import welcome_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = welcome_pb2_grpc.WelcomeServiceStub(channel)
        name = input("Enter your name: ")
        response = stub.SayWelcome(welcome_pb2.WelcomeRequest(name=name))
        print(response.message)

if __name__ == '__main__':
    run()
