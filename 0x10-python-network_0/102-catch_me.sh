#!/bin/bash
#makes a request to 0.0.0.0:5000/catch_me
curl -s 0.0.0.0:5000/catch_me -w 'You got me!' -o /dev/null
