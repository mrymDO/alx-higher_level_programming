#!/bin/bash
#send a POST request with the contents of a file
curl -X POST "$1" -H "Content-Type: application/json" -d @"$2"
