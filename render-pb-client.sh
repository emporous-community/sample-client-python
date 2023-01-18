#!/bin/bash

set -x
SRC_DIR=.
DST_DIR=.
#PYI_DIR=types

python -m grpc_tools.protoc -I"$SRC_DIR" --python_out="$DST_DIR" --pyi_out="$DST_DIR" --grpc_python_out="$DST_DIR" "$SRC_DIR/manager.proto"
