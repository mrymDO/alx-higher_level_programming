#!/bin/bash
#send a POST request with the contents of a file
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
