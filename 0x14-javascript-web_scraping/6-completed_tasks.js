#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const taskByUser = {};

    for (const task of data) {
      if (task.completed) {
        if (taskByUser[task.userId]) {
          taskByUser[task.userId]++;
        } else {
          taskByUser[task.userId] = 1;
        }
      }
    }
    console.log(taskByUser);
  }
});
