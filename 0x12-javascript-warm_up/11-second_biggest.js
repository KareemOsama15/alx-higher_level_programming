#!/usr/bin/node
if (process.argv.length <= 3) {
    console.log(0);
} else {
    let first = parseInt(process.argv[2]);
    let second = first;
    let current = 0;
    for (let i = 3; i < process.argv.length; i++) {
        current = parseInt(process.argv[i]);
        if (current > first) {
            second = first;
            first = current;
        }
    }
    console.log(second);
}
