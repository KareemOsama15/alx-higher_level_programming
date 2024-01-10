#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length;
  const mid = len / 2;
  for (let i = 0; i < mid; i++) {
    const temp = list[len - i - 1];
    list[len - i - 1] = list[i];
    list[i] = temp;
  }
  return list;
};
