const express = require("express");
const Contact = require("../models/contact_model");
const ContactController = require("../controllers/homePageController");

// ROUTER
const router = express.Router();

// render routes
router.get("/", ContactController.homePage);
router.get("/add-contact", (req, res) => {
  res.render("add-contact");
});
router.get("/update-contact/:id", ContactController.getContactById);
router.get("/show-contact/:id", ContactController.showContact);

// delete
router.get("/delete-contact/:id", ContactController.deleteContact);

// create contact
router.post("/add-contact", ContactController.addContact);

// update contact
router.post("/update-contact/:id", ContactController.updateContact);

// export
module.exports = router;
