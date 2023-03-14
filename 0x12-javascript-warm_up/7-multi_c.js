#!/usr/bin/node
const loopT = parseInt(process.argv[2]);
let i;
if (isNaN(loopT)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < loopT; i++) {
    console.log('C is fun');
  }
}
