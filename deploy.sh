#!/bin/bash

cd ../
cp fxTrade/deploy.sh ./
cp fxTrade/Dockerfile ./

docker build -t auto_order/ubuntu:1.0 .
echo "builded docker images."

docker run -i -t auto_order/ubuntu:1.0 /bin/bash
