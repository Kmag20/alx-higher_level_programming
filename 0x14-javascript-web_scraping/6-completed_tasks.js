#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const data = JSON.parse(body);
    const objDict = new Object();
    for (let i = 1; i <= 10; ++i) {
      objDict[i.toString()] = 0;
    }
    data.forEach(todo => {
      if (todo['completed']) {
        idStr = todo['userId'].toString();
	objDict[idStr] += 1;
      }
    });
  console.log(objDict);
  }
});
