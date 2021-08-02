#!/usr/bin/node

function factorial (nb) {
  if (nb === 1 || isNaN(nb)) {
    return 1;
  }
  return nb * factorial(nb - 1);
}
const ar = process.argv[2];
const f = factorial(parseInt(ar));
console.log(f);
