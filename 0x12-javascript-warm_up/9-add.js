#!/usr/bin/node

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return NaN;
  } else {
    return (a + b);
  }
}
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

console.log(add(a, b));
