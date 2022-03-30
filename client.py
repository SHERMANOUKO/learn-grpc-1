from urllib import response
import grpc

import calculator_pb2
import calculator_pb2_grpc

# open a grpc channel
channel = grpc.insecure_channel('localhost:50051')

# create a valid request message
number = calculator_pb2.Number(value=16)

stub = calculator_pb2_grpc.CalculatorStub(channel)
print
# make the call
reponse = stub.SquareRoot(number)

print(response.value)
