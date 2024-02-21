#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const options = {
  url: 'https://swapi-api.alx-tools.com/api/films/' + filmId,
  method: 'GET'
};

request(options, (err, res, body) => {
  if (err) { console.log(err); } else {
    const characters = JSON.parse(body).characters;
    characters.forEach(charUrl => {
      request(charUrl, (err, res, body) => {
        if (err) { console.log(err); } else {
          const name = JSON.parse(body).name;
          console.log(name);
        }
      });
    });
  }
});
