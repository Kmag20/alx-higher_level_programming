#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request.get(url, function (err, res, data) {
  console.log(err || JSON.parse(data).title);
});
