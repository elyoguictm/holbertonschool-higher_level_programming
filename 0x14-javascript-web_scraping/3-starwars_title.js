#!/usr/bin/node
const request = require('request');
const argv = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + argv;
request(url, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  console.log(JSON.parse(body).title);
});
