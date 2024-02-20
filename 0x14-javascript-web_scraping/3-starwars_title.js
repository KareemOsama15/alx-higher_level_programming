#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const options = {
  url: 'https://swapi-api.alx-tools.com/api/films/' + id,
  method: 'GET'
};
request(options, (err, res, body) => {
  if (err) { console.log(err); } else {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
