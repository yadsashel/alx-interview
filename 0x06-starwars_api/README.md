# 0x06. Star Wars API

## Description
This project requires you to create a script that interacts with the Star Wars API to fetch and display information about characters from a specified Star Wars movie. You will need to retrieve data from an external API and handle asynchronous operations using JavaScript.

## Requirements
- **Platform**: Ubuntu 20.04 LTS
- **Node.js Version**: 10.14.x
- **Coding Style**: Must be semistandard compliant, with semicolons and following AirBnB style.
- **Modules Used**: `request` module for HTTP requests.
- **File Standards**: All files should end with a new line and must be executable. Do not use `var` for variable declarations.
  
## Installation
1. **Install Node.js 10**:
   ```bash
   curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
   sudo apt-get install -y nodejs
   ```

2. **Install semistandard**:
   ```bash
   sudo npm install semistandard --global
   ```

3. **Install request module**:
   ```bash
   sudo npm install request --global
   export NODE_PATH=/usr/lib/node_modules
   ```

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/alx-interview
   cd alx-interview/0x06-starwars_api
   ```

2. Make the script executable:
   ```bash
   chmod +x 0-starwars_characters.js
   ```

3. Run the script with a Movie ID as an argument:
   ```bash
   ./0-starwars_characters.js <MovieID>
   ```
   - Example:
     ```bash
     ./0-starwars_characters.js 3
     ```
     Output:
     ```
     Luke Skywalker
     C-3PO
     R2-D2
     Darth Vader
     Leia Organa
     Obi-Wan Kenobi
     Chewbacca
     Han Solo
     Jabba Desilijic Tiure
     Wedge Antilles
     Yoda
     Palpatine
     Boba Fett
     Lando Calrissian
     Ackbar
     Mon Mothma
     Arvel Crynyd
     Wicket Systri Warrick
     Nien Nunb
     Bib Fortuna
     ```

## Script: `0-starwars_characters.js`
This script prints all characters of a given Star Wars movie, as specified by the movie ID. It interacts with the Star Wars API to fetch data in the order that characters are listed in the `/films/` endpoint.

### Example Code
```javascript
#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) console.error(error);
  else {
    const characters = JSON.parse(body).characters;
    characters.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (error) console.error(error);
        else console.log(JSON.parse(body).name);
      });
    });
  }
});
```

### Explanation
1. **Command-line Argument**: Accepts the Movie ID as a command-line argument.
2. **API Request**: Fetches the movie details from the Star Wars API `/films/` endpoint using the provided Movie ID.
3. **Character List**: Parses the response to retrieve the character URLs and makes a separate API request for each URL to get character names.
4. **Asynchronous Execution**: Uses asynchronous requests to ensure all character data is fetched and displayed in the order it appears in the API.

## Concepts Needed
- **HTTP Requests in JavaScript**: Make HTTP requests using the `request` module.
- **Working with APIs**: Understand RESTful API structure, JSON parsing, and data manipulation.
- **Asynchronous Programming**: Manage asynchronous data with callbacks and handle API response data.
- **Command Line Arguments in Node.js**: Use `process.argv` to access arguments passed to the Node.js script.
- **Array Manipulation and Iteration**: Iterate over arrays to display character names in the correct order.

## Additional Resources
- **Node.js Documentation**: [Node.js HTTP requests](https://nodejs.org/api/http.html)
- **JavaScript Promises and async/await**: [Asynchronous Programming in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous)

## Project Repository
- **GitHub Repository**: [alx-interview](https://github.com/yourusername/alx-interview)
- **Directory**: `0x06-starwars_api`
- **File**: `0-starwars_characters.js`
