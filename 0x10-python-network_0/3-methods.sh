#!/bin/bash
#displays all HTTP methods the server will accept
curl -X OPTIONS "$1"
