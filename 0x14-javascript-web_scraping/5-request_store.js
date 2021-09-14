#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const argv = process.argv[2];
const argu = process.argv[3];
request(argv, function (err, resp, body) {
  if (err) throw err;
  fs.writeFile(argu, body, 'utf8', function (err, data) {
    if (err) throw err;
  });
});
