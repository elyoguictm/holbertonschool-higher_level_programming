#!/usr/bin/node
const argu = process.argv[2];
const request = require('request');
request(argu, function (err, resp) {
  if (err) throw err;
  console.log('code: ' + resp.statusCode);
});
