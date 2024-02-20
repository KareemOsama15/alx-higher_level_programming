#!/usr/bin/node

const request = require('request');
const options = {
  url: process.argv[2],
  method: 'GET'
};
request(options, (err, res) => {
  if (err) { console.log(err); } else { console.log('code: ' + res.statusCode); }
});
