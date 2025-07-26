const express = require("express");
const path = require("path");
const ejs = require("ejs");
const contactRouter = require("./routes/contactRouter");
const morgan = require("morgan");
const dotenv = require("dotenv");
dotenv.config({ path: "./config.env" });
const connectDB = require("./database");

// DATABASE
connectDB();
// APP
const app = express();

// MIDDLEWARES
app.use(express.json()); // <-- Needed to parse JSON bodies
app.use(morgan("dev"));
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");
app.use(express.static(path.join(__dirname, "public")));
app.use(express.urlencoded({ extended: false }));

// ROUTER
app.use("/", contactRouter);

// SERVER
app.listen(3500, () => {
  console.log("Server is running link http://localhost:3500");
});
