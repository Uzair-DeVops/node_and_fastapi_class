const express = require('express');
const ejs = require("ejs");
const fs = require("fs");




const app = express();



data =  fs.readFileSync("productsData.json", "utf-8");
const jsonData = JSON.parse(data);




app.set("view engine", "ejs");
app.set("views", "views");





app.get("/products", (req, res) => {
    res.render("products", { jsonData });
    // TODO: Write your code here
})



app.listen(3070, () => {
    console.log("Server is running on this server http://localhost:3070");
});