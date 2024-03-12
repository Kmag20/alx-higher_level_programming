#!/usr/bin/node

module.exports = class Square extends require('./5-square.js') {
  constructor (size) {
    super(size, size);
  }

  charPrint () {
    for (let i = 0; i < this.size; i++) console.log('c'.repeat(this.size));
  }
};
