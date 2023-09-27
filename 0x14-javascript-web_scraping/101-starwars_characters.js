#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    printCharactersInOrder(characters, 0);
  }
});

function printCharactersInOrder (characters, index) {
  if (index >= characters.length) {
    return;
  }

  const characterUrl = characters[index];
  request.get(characterUrl, (err, response, body) => {
    if (err) {
      console.error(err);
    } else {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      // Continue with the next character
      printCharactersInOrder(characters, index + 1);
    }
  });
}
