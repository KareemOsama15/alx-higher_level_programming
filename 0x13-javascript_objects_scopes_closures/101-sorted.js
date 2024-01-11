#!/usr/bin/node
const dictobj = require('./101-data').dict;
const newdict = {};
for (const [key, value] of Object.entries(dictobj)) {
  if (!newdict[value]) {
    newdict[value] = [];
  }
  newdict[value].push(key);
}
console.log(newdict);
