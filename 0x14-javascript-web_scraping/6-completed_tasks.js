#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const data = JSON.parse(body);
    const objDict = {};
    let highest_id = 0;
    data.forEach(todo => {
      if (todo['userId'] > highest_id) {
        highest_id = todo['userId'];
      }
    });
    for (let i = 1; i <= highest_id; ++i) {
      objDict[i.toString()] = 0;
    }
    data.forEach(todo => {
      if (todo.completed) {
        const idStr = todo.userId.toString();
        objDict[idStr] += 1;
      }
    });

    const flattenedValues = Object.values(objDict);
    if (flattenedValues.every(num => num === 0)) {
      console.log('{}');
    } else {
      console.log(objDict);
    }
  }
});
