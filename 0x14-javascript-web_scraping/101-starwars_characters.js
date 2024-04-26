#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const index = parseInt(process.argv[2], 10);
request.get(url, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const data = JSON.parse(body);
    const characters = data.results[index].characters;
    characters.forEach(character => {
      request.get(character, (err, res, body) => {
        if (!err && res.statusCode === 200) {
          const charName = JSON.parse(body).name;
          console.log(charName);
        }
      });
    });
  }
});
