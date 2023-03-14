#!/usr/bin/node
if (process.argv.length <= 2 || process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
