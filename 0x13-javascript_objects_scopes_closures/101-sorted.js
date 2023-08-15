#!/usr/bin/node

const initialDict = require('./101-data').dict;
const newDict = {};

for (const [userId, occurrences] of Object.entries(initialDict)) {
  if (!(occurrences in newDict)) {
    newDict[occurrences] = [];
  }
  newDict[occurrences].push(userId);
}
console.log(newDict);
