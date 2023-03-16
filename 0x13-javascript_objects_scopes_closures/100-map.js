#!/usr/bin/node
const list = require('./100-data').list;
let i = 0;
console.log(list);
console.log(list.map(x => x * i++));
