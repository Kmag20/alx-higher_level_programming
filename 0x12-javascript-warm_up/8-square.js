#!/usr/bin/node

const square = parseInt(process.argv[2], 10);

if (!isNaN(square) && square >= 0) {
  for (let i = 0; i < square; i++) {
    let line = '';
    for (let j = 0; j < square; j++) {
      line += 'X';
    }
    console.log(line);
  }
}
