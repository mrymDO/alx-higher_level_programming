#!/bin/bash
#send a POST request with the contents of a file
curl -X POST -H "Content-Type: application/json" -d @"$2" "$1"
