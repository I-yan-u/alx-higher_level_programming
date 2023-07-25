#!/usr/bin/node
const r = require('request');

const Id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';

r(url + Id, (err, response, body) => {
  if (err !== null) {
    console.log(err);
  }
  console.log(JSON.parse(body).title);
});
