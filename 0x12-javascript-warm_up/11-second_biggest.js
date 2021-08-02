#!/usr/bin/node

const args = process.argv.slice(2);
if (args.length > 1) {
  args.sort(function (a, b) { return b - a; });
  console.log(args[1]);
} else {
  console.log('0');
}
