#!/usr/bin/nodejs

const file = require('fs');
file.readFile(process.argv[2], 'utf8', function (error, content){
	console.log(error || content);
});