# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC calculator.Greeter client."""

from __future__ import print_function

import grpc

import calculator_pb2
import calculator_pb2_grpc as calculator_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        print("Insert first number : ")
        x=int(input())
        print("Insert second number : ")
        y=int(input())
        response = stub.add(calculator_pb2.CalculationRequest(input1=x, input2=y))
        print("Addition of "+str(x)+" and "+str(y)+" is : "+ str(response.result))
    
if __name__ == '__main__':
    run()
