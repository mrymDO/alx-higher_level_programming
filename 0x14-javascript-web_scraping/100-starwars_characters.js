#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const characterUrl of characters) {
      request.get(characterUrl, (err, response, body) => {
        if (err) {
          console.error(err);
        } else {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    }
  }
});
