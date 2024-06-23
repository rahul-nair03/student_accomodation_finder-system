const {execSync} = require("node:child_process");
const express = require("express");
const cors = require("cors");
const app = express();

app.use(cors());

app.post("/search", async (req, res) => {
    const query = req.query;
    const hostelName = query.hostelName; 

    const processRes = execSync(`python new.py "${hostelName}"`, {cwd : "../python", encoding : "utf-8"});
    const output = processRes.split("\r\n");
     
    const neededOutput = [output.at(0), output.at(1), output.at(2)].map((line) => {
        const [hostelName, location, rating, price, gender] = line.split(",");

        return {hostelName, location, rating, price, gender};
    });
    

    return res.json(neededOutput);
})



app.listen(8080, () => {
    console.log("Started server on Port 8080")
})

