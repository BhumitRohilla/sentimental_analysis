const path = require('path');
const fs = require('fs');

const filesInResponse = fs.readdirSync(path.join(__dirname, './response'));


const result = [];

filesInResponse.forEach((fileName) => {
    try {
        let fileResult = fs.readFileSync(path.join(__dirname, `/response/${fileName}`));
        fileResult = fileResult.toString()
        fileResult = JSON.parse(fileResult)
        fileResult.data.search_by_raw_query.search_timeline.timeline.instructions.forEach((data) => {
            (data?.entries ?? []).forEach((element) => {
                result.push(element);
            })
        })
        result.push()
    } catch (error) {
        console.log(error);
        console.log(fileName);
    }
})


fs.writeFileSync(path.join(__dirname, './combined.json'), JSON.stringify(result))
