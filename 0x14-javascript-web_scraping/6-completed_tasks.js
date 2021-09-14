#!/usr/bin/node
const request = require('request');
const argv = process.argv[2];
request(argv, function (error, response, body) {
  if (error) throw error;
  const user = {};
  for (const task of JSON.parse(body)) {
    if (task.completed) {
      if (user[task.userId]) {
        user[task.userId]++;
      } else {
        user[task.userId] = 1;
      }
    }
  }
  console.log(user);
});
