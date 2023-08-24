#!/bin/bash

docker build -t animage .

docker run  -p 5001:5000 animage