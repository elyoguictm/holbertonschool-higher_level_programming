#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];
  for (let index = (list.length - 1); index >= 0; index--) {
    rev.push(list[index]);
  }
  return rev;
};
