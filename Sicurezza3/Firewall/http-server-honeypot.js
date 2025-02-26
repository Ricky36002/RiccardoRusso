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

app.all("*", (req, res) => {
  console.log(req.url, req.headers);
  console.log("SONO HONEYPOT");
  res.send("OK");
});

let options = {};

let host = "192.168.122.1";
let port = 4000;

http.createServer(options, app).listen(port, host, () => {
  console.log("HTTP server running at http://localhost:4000");
});
