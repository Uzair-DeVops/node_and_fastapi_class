const mongoose = require("mongoose");


const contactSchema = mongoose.Schema({
    firstName: {
        type: String,
    },
    lastName: {
        type: String,
    },
    email: {
        type: String,
    },
    phone: {
        type: String,
    },
    address: {
        type: String,
    }
});


const contact = mongoose.model("Contact", contactSchema);


module.exports = contact;