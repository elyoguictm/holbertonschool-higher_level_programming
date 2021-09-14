#!/usr/bin/node
const request = require('request');
const argv = process.argv[2];
request(argv, function (err, resp, body) {
  if (err) throw err;
  let count = 0;
  for (const film of JSON.parse(body).results) {
    for (const character of film.characters) {
      if (character.includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
