#!/usr/bin/node

let i;
if (!parseInt(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('C is fun');
  }
}
