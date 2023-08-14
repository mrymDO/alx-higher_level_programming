#!/usr/bin/node

function fact (n) {
  if (isNaN(n)) {
    return 1;
  }

  if (n === 0) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}

const num = parseInt(process.argv[2]);
console.log(fact(num));
