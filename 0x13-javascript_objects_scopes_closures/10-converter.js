#!/usr/bin/node
exports.converter = function (base) {
  function numb (nb) {
    return nb.toString(base);
  }
  return numb;
};
