const express = require("express");
const fs = require("fs");
const jsonData = require("../data.json");
const productControllers = require("../controllers/productControllers");




router = express.Router();



// routes
router
.get("/", productControllers.readAllProducts)
.post("/", productControllers.createNewProduct);


router
.get("/:id", productControllers.getProductById)
.patch("/:id", productControllers.updateProductById)
.delete("/:id", productControllers.deleteProductById);




module.exports = router;