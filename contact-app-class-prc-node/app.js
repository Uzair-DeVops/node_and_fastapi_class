import express from "express";
import dotenv from "dotenv";
import morgan from "morgan";
import connectDB from "./database.js";
import ejs from "ejs";
import contactRoutes from "./routes/contactRoutes.js";

// DOTENV
dotenv.config({ path: "./config.env" });


// DATABASE
connectDB();




// APP
const app = express();

// engine
app.set("view engine", "ejs");
app.set("views", "./views");
app.use(express.static("./public"));

// MIDDLEWARES
app.use(morgan("dev"));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));



// ROUTERS
app.use("/", contactRoutes);






// EXPORT
export default app;
