#!/usr/bin/node

const fs = require('fs');

fs.readFile('cisfun', 'utf-8', function (err, data) {
  if (err) {
    console.error(err);
  }
  console.log(data);
});
