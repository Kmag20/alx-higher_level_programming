#!/usr/bin/node

const size = parseInt(process.argv[2], 10);
if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    console.log('C is fun');
  }
} else if (process.argv.length <= 2) {
  console.log('Missing number of occurrences');
}
