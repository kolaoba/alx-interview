#!/usr/bin/node
// Script that prints all characters of a Star Wars movieId
const request = require('request');

const url = 'https://swapi.dev/api/films/';
const args = process.argv.slice(1);

if (args.length < 2) {
  console.log('Error');
  process.exit(1);
};

const movieId = args[1];
  request(`${url}${movieId}`, (err, res, body) => {
    if (err) {
      console.error(err);
    } else {
      const data = JSON.parse(body);
      const characters = data.characters;
      const characterNames = characters.map(characterUrl => {
        return new Promise((resolve, reject) => {
          request(characterUrl, (err, res, body) => {
            if (err) {
              reject(err);
            } else {
              const characterData = JSON.parse(body);
              resolve(characterData.name);
            }
          });
        });
      });
      Promise.all(characterNames).then(names => {
        names.forEach(name => console.log(name));
      });
    }
  });
