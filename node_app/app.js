const express = require('express');


// reqs () , res ()







const app = express();



app.get("/" , (req, res) => {
  res.send("<h1>Hello, World!<h1/>");
})

app.get("/about/:id", (req, res) => {
  res.send(req.params , req.query);
});

app.get("/about/profile", (req, res) => {
  res.send("<h1>profile Page</h1>");
});
app.get("/contact", (req, res) => {
  res.send("<h1>Contact Page</h1>");
});

app.get("/help", (req, res) => {
  res.send("<h1>Help Page</h1>");
});






app.listen(3001, () => {
  console.log('Server is running on port 3001');
});