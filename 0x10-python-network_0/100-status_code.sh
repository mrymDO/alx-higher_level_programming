#!/bin/bash
#Displays the status code of response of an HTTP request
curl -s -o /dev/null -w "%{http_code}" "$1"
