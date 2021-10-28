#!/usr/bin/node

const id = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
const option = { json: true };

request(url, option, (error, res, body) => {
  if (error) {
    return console.log(error);
  }
  if (!error && res.statusCode === 200) {
    body.characters.forEach(element => {
      request(element, option, (error, res, body) => {
        if (error) {
          return console.log(error);
        }
        if (!error && res.statusCode === 200) {
          console.log(body.name);
        }
      });
    });
  }
});
