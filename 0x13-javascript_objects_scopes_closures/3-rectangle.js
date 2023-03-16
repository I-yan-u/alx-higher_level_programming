#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let row; let col;
    for (row = 0; row < this.height; row++) {
      let out = '';
      for (col = 0; col < this.width; col++) {
        out += 'X';
      }
      console.log(out);
    }
  }
}
module.exports = Rectangle;
