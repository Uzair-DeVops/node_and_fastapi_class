const fs = require("fs");

const data = fs.readFileSync("data.json", "utf-8");
const jsonData = JSON.parse(data);

exports.readAllProducts = (req, res) => {
  res.send(jsonData);
};

exports.createNewProduct = (req, res) => {
  const newProduct = req.body;
  // id generation logic
  let lastId = 0;
  jsonData.forEach((product) => {
    if (product.id > lastId) {
      lastId = product.id;
    }
  });
  newProduct.id = lastId + 1;
  jsonData.push(newProduct);
  fs.writeFileSync("data.json", JSON.stringify(jsonData, null, 2));
  res.json(newProduct);
};

exports.getProductById = (req, res) => {
  const productId = req.params.id;
  const product = jsonData.find((product) => product.id == productId);
  res.json(product);
};

exports.updateProductById = (req, res) => {
  const productId = req.params.id;
  const newData = req.body;
  let product = jsonData.find((product) => product.id == productId);
  product = { ...product, ...newData };
  jsonData.forEach((item, index) => {
    if (item.id == productId) {
      jsonData[index] = product;
    }
  });
  fs.writeFileSync("data.json", JSON.stringify(jsonData, null, 2));
  res.json(product);
};

exports.DeleteProductById = (req, res) => {
  const productId = req.params.id;
  jsonData.forEach((product, index) => {
    if (product.id == productId) {
      jsonData.splice(index, 1);
    }
  });
  fs.writeFileSync("data.json", JSON.stringify(jsonData, null, 2));
  res.send("Product deleted");
};
