#!/usr/bin/node
const request = require('request');
const fs = require('fs');
url = process.argv[2];
outputFile = process.argv[3];
request.get(url,  (err, res, body) => {
  if (!err && res.statusCode === 200) {
    fs.writeFile(outputFile, body, (err) => {
      if (err) console.error(err);
    });
  } else {
    console.error(err);
  }
});
