#!/usr/bin/nodejs

const file = require('fs');

const print = function (error, content){console.log(error || content);};
const content = file.readFile(process.argv[2], 'utf8', print);