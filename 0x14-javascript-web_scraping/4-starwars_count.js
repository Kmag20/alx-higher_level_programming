#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const wedgeAntillesURL = 'https://swapi-api.alx-tools.com/api/people/18/';

request.get(url, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const data = JSON.parse(body);
    const results = data.results;

    const moviesWithWedgeAntilles = results.filter(movie => {
      const characters = movie.characters;
      return characters.some(character => character.includes('/18/');
    });

    console.log(`${moviesWithWedgeAntilles.length}`);
  } else {
    console.error(err);
  }
});
