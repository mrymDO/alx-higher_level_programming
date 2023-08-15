#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.log('Usage: ./102-concat.js <file1> <file2> <destination>');
  process.exit(1);
}

const content1 = fs.readFileSync(process.argv[2], 'utf-8');
const content2 = fs.readFileSync(process.argv[3], 'utf-8');

fs.writeFileSync(process.argv[4], content1 + content2);
