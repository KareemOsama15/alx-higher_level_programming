#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) { console.log(err); } else {
    const results = JSON.parse(body).results;
    const characterFilms = results.filter(film =>
      film.characters.includes(
        'https://swapi-api.alx-tools.com/api/people/18/')
    );
    console.log(characterFilms.length);
  }
});

// another solution of 2 loops
// let count = 0;
// for (let i = 0; i < results.length; i++) {
//   for (const film of results[i].characters) {
//     if (film.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
//       count++;
//       break;
//     }
//   }
// }
// console.log(count);
