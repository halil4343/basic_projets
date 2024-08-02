const fs = require('fs');

fs.readFile('myJSProject/unnamedProject/arts.json', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    const asciiArt = JSON.parse(data);

    for (const [key, value] of Object.entries(asciiArt)) {
        console.log(`${key}:\n${value}\n`);
    }
});
