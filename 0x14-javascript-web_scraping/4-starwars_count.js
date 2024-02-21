#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) { console.log(err); } else {
    const results = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < results.length; i++) {
      for (const film of results[i].characters) {
        if (film.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  }
});

// another solution instead of 2 loops
// const character_films = results.filter(film =>
//     film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
// )
// console.log(character_films.length)
