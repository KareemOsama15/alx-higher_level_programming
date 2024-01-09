#!/usr/bin/node
const convertNum = parseInt(process.argv[2]);
if (!isNaN(convertNum)) {
  console.log('My number: ' + convertNum);
} else {
  console.log('Not a number');
}
