#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map(myFunction);
function myFunction (currentValue, idx) {
  return currentValue * idx;
}
console.log(list);
console.log(newList);
