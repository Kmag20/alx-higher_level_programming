#!/usr/bin/node

const param = process.argv[2];
const intParam = parseInt(param, 10);

if (!isNaN(intParam)) {
  console.log(`My number: ${intParam}`);
} else {
  console.log('Not a number');
}
