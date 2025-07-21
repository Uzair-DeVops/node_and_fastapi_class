const express = require("express") 
const connectDB = require("./database")
const dotenv = require("dotenv")
const productRoutes = require("./routes/produtRoutes")
const morgan = require("morgan")

dotenv.config({ path: "./config.env" });

const app = express() ;


app.use(morgan('dev'));
app.use(express.json());

connectDB.connectToDatabase();



app.use('/products', productRoutes);







app.listen(3500, () => {
    console.log("Server is on this url http://localhost:3500");
});





























































































// require("dotenv").config({ path: "./config.env" });
// const connectDB = require("./database");
// const express = require("express");
// const app = express();
// const product = require("./models/product_schema");
// connectDB();

// app.use(express.json());

// app.get("/", async (req, res) => {
//   const data = await product.find({});
//   res.send(data);
// });

// // create product

// app.post("/products", async (req, res) => {
//   const newProduct = await product.create(req.body);
//   res.status(201).send({
//     message: "Product created successfully",
//     product: newProduct,
//   });
// });

// // get product by id

// app.get("/products/:id", async (req, res) => {
//   const data = await product.findById(req.params.id);
//   if (!data) {
//     return res.status(404).send({ message: "Product not found" });
//   }
//   res.send(data);
// });

// // update product by id

// app.patch("/products/:id", async (req, res) => {
//   const data = await product.findByIdAndUpdate(req.params.id, req.body);
//   // return new data

//   const newData = await product.findById(req.params.id);

//   if (!data) {
//     return res.status(404).send({ message: "Product not found" });
//   }
//   res.send(newData);
// });

// app.listen(3000, () => {
//   console.log("Server is running on port 3000");
// });



