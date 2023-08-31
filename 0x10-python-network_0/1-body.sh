#!/bin/bash
#Get request
response=$(curl -s -o /dev/stdout -w "%{http_code}" "$1")
http_code="${response: -3}"
if [ "$http_code" -eq 200 ];
then
    curl -s "$1"
fi
