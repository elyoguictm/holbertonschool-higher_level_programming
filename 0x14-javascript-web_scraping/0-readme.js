#!/usr/bin/node
const argv = process.argv[2];
const fs = require('fs');
fs.readFile(argv, 'utf8', (err, data) => {
  if (err) {
    return console.error(err);
  }
  console.log(data);
});
