#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.log(`Error fetching movie: ${error ? error.message : response.statusCode}`);
    return;
  }

  const characters = JSON.parse(body).characters;
  const names = [];

  function getCharacterName(index) {
    if (index >= characters.length) {
      console.log(names.join('\n'));
      return;
    }

    const characterUrl = characters[index];
    request(characterUrl, (error, response, body) => {
      if (error || response.statusCode !== 200) {
        console.log(`Error fetching character: ${error ? error.message : response.statusCode}`);
        return;
      }

      const characterName = JSON.parse(body).name;
      names.push(characterName);
      getCharacterName(index + 1);
    });
  }

  getCharacterName(0);
});
