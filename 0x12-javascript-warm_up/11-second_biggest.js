#!/usr/bin/node
if (process.argv.length === 3 || process.argv[2] === undefined) {
    console.log(0);
}
let first = parseInt(process.argv[2]);
let second = 0;
let current = 0;
for (let i = 3; i < process.argv.length; i++) {
    current = parseInt(process.argv[i]);
    if (process.argv[i] > first) {
        second = first;
        first = current;
    }
}
console.log(second);
