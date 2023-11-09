#!/usr/bin/node

const request = require('request');

function getMovieCharacters(movieId) {
    // Define the base URL for the Star Wars API
    const baseUrl = "https://swapi-api.alx-tools.com/api/films/";

    // Make a request to the API to get the movie information
    request(baseUrl + movieId, (error, response, body) => {
        if (!error && response.statusCode === 200) {
            const movieData = JSON.parse(body);
            const characters = movieData.characters || [];

            if (characters.length > 0) {
                characters.forEach(characterUrl => {
                    // Get character information
                    request(characterUrl, (error, characterResponse, characterBody) => {
                        if (!error && characterResponse.statusCode === 200) {
                            const characterData = JSON.parse(characterBody);
                            const characterName = characterData.name;
                            console.log(characterName);
                        } else {
                            console.log(`Failed to fetch character data for ${characterUrl}`);
                        }
                    });
                });
            } else {
                console.log("No characters found for this movie.");
            }
        } else {
            console.log("Failed to fetch movie data.");
        }
    });
}

// Usage: node script.js <Movie ID>
if (process.argv.length !== 3) {
    console.log("Usage: node script.js <Movie ID>");
    process.exit(1);
}

const movieId = process.argv[2];
getMovieCharacters(movieId);
