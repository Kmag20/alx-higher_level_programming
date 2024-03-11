#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const items = [];
  const itemLength = process.argv.length;
  for (let i = 2; i < itemLength; i++) {
    items.push(parseInt(process.argv[i]));
  }
  items.sort((a, b) => b - a);
  console.log(items[1]);
}
