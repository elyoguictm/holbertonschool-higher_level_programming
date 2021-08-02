#!/usr/bin/node

let i, j;
if (!parseInt(process.argv[2])) {
  console.log('Missing size');
} else {
  for (i = 0; i < process.argv[2]; i++) {
    for (j = 0; j < process.argv[2]; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
