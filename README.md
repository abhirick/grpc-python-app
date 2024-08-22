# grpc-python-app
Sample Python GRPC App

pip3 install virtualenv
virtualenv <your-env>
source <your-env>/bin/activate



pip install grpcio grpcio-tools protobuf
pip install grpcio-reflection

grpcurl -plaintext -d '{"name": "John Doe"}' localhost:50051 welcome.WelcomeService/SayWelcome
