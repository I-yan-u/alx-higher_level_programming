#!/usr/bin/node

let loopT = parseInt(process.argv[2]);
let row;
let col;

if (isNaN(loopT)) {
    console.log('Missing number of occurrences');
} else {
    for (row = 0; row < loopT; row++) {
        let square = '';
	for (col = 0; col < loopT; col++) {
	    square += 'x';
	}
    console.log(square);
    }
}
