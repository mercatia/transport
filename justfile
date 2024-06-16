

protos:
    #!/bin/bash

    python -m grpc_tools.protoc -I../bazaar-engine/engine/src/main/proto --python_out=./transport/protos --grpc_python_out=./transport/protos  ../bazaar-engine/engine/src/main/proto/transport.proto