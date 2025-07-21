const mongoose = require('mongoose');



const productSchema =  mongoose.Schema({
    name: {
        type: String,
        required: true,
    },
    category: {
        type: String,
    },
    brand: {
        type: String,
    },
    price: {
        type: Number,
    },
    inStock: {
        type: Boolean,
    },
    rating: {
        type: Number,
    }});



const Product = mongoose.model('products', productSchema);

// init logic



module.exports = Product