#!/usr/bin/node

let i;

if (process.argv.length < 3) {
    console.log("No Argument");
} else if (process.argv.length === 3) {
    console.log(process.argv[0]);
} else {
    for (i = 2; i < process.argv.length; i++) {
        console.log(process.argv[i]);
    }
}
