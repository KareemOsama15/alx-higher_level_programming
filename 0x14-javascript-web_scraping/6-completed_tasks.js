#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) { console.log(err); }
  const data = JSON.parse(body);
  const newdict = {};
  for (let i = 0; i < data.length; i++) {
    const key = data[i].userId;
    if (data[i].completed === true) {
      if (newdict[key] === undefined) {
        newdict[key] = 0;
      }
      newdict[key]++;
    }
  }
  console.log(newdict);
});
