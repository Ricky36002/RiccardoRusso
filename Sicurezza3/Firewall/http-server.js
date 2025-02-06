/*
npm i express
npm i eventsource
*/

const http = require("http");
const fs = require("fs");
const express = require("express");
const app = express();

// Serve static files
app.use(express.static("./"));

// Example Addizionatore
app.get("/api", (req, res) => {
    // GET /api?add1=10&add2=20
    let add1 = req.query.add1;
    let add2 = req.query.add2
    let user = req.query.username;
    console.log(add1,add2,user);
    if (user === "user01") {
        res.json({ risposta: add1 + add2});  
    } else{
        res.json({ risposta: add2 + add1});
    }
});

let options = {};

let host = "172.21.68.6";
let port = 3000;

http.createServer(options, app).listen(3000, "172.21.68.6", () => {
  console.log("HTTP server running at https://172.21.68.6:3000");
});
