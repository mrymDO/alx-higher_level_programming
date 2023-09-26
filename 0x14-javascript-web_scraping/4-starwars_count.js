#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    let movieCount = 0;
    for (const movie of movieData.results) {
      if (movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        movieCount++;
      }
    }
    console.log(`${movieCount}`);
  }
});
