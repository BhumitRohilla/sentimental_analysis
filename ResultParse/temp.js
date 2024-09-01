const fs = require('fs');
const path = require('path');

const readResult = JSON.parse(fs.readFileSync(path.join(__dirname, './HashTag.json')).toString());

readResult.forEach((element) => {
    element.tweetId = element["Tweet Reference"].split('/').pop().trim()
    delete element["Tweet Reference"]
})

fs.writeFileSync(path.join(__dirname, './HashTag.json'), JSON.stringify(readResult));