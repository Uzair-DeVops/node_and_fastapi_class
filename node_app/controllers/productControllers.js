const fs = require("fs");
const Product = require("../models/product_schema");


exports.readAllProducts = async (req, res) => {
  const data = await Product.find();
  res.status(200).send(data);
};



exports.createNewProduct = async (req, res) => {
  const newData = req.body;
  console.log(newData);
  await Product.create(newData);
  res.status(201).json({
   message: "Product created successfully",
   data: newData
 });
};



exports.getProductById = async (req, res) => {
  const productId = req.params.id;
  const data = await Product.findById(productId);
  res.status(200).send(data);
};



exports.updateProductById = async (req, res) => {
  const productId = req.params.id;
  const data = req.body;
  const updatedProduct = await Product.findByIdAndUpdate(productId, data, { new: true });

  if (!updatedProduct) {
    return res.status(404).json({ message: "Product not found" });
  }

  res.status(200).json({
    message: "Product updated successfully",
    newData: updatedProduct.toObject()
  });
};



exports.deleteProductById = async (req, res) => {
  const productId = req.params.id;

  const product = await Product.findById(productId);
  if (!product) {
    return res.status(404).json({ message: "Product not found" });
  }

  const data = await Product.deleteOne(product);
  res.status(200).send({
    message: "Product deleted successfully",
  });
  
};
