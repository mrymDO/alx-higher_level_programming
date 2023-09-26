#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (error, reponse) => {
  if (error) {
    console.error('Error: ', error);
  } else {
    console.log(`Code: ${reponse.statusCode}`);
  }
});
