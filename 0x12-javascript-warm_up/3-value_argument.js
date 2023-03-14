#!/usr/bin/node
if (process.argv.length <= 2 || process.argv[2] === undefined) {
  console.log('No Argument');
} else {
  console.log(process.argv[2]);
}
