#!/bin/bash

version=$1

if [[ -z version ]];then
    echo "missing parameters"
    exit 1
fi

docker build -t chatapp:$version .

docker run  -p 5000:5000 chatapp