#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    let row; let col;
    for (row = 0; row < this.height; row++) {
      let str = '';
      for (col = 0; col < this.width; col++) {
        str += c;
      }
      console.log(str);
    }
  }
}

module.exports = Square;
