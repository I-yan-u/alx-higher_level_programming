#!/usr/bin/node
exports.esrever = function (list) {
  let i;
  let lent = list.length;
  const rList = [];
  for (i = 0; i < list.length; i++) {
    rList[lent - 1] = list[i];
    lent--;
  }
  return rList;
};
