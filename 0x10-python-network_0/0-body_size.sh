#!/bin/bash
#Content length of http headers
curl -sI "$1" | grep -iF 'Content-Length' | awk '{print $2}'
