#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const id = 18;

request(url, (err, res, body) => {
  if (err) { console.log(err); } else {
    const results = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < results.length; i++) {
      for (const film of results[i].characters) {
        if (film.includes('https://swapi-api.alx-tools.com/api/people/' + id)) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  }
});
