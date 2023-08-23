#!/bin/bash

docker build -t animage .

docker run -d -p 5005:5000 animage