const express = require('express');
const morgan = require('morgan');
const productRoutes = require('./routes/produtRoutes.js');

// app setup
const app = express();


// Middleware
app.use(morgan('dev'));
app.use(express.json());


// subapps
app.use('/products', productRoutes);

// Controllers



// Sevrer setup
PORT = 3505;
app.listen(PORT, () => {
  console.log(`Server is on this url http://localhost:${PORT}`);
});
