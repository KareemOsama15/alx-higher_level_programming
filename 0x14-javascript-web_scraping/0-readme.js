#!/usr/bin/node

const path = process.argv[2];
const fs = require('fs');
fs.readFile(path, 'utf8', (err, data) => {
  if (err) { console.log(err); } else { console.log(data); }
});
