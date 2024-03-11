#!/usr/bin/node

module.exports = function (number, theFunction) {
  theFunction(++number);
};
