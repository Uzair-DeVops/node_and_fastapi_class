const Contact = require("../models/contact_model");

module.exports.homePage = async (req, res) => {
  const contacts = await Contact.find();
  res.render("home", { contacts });
};

module.exports.showContact = async (req, res) => {
  const contact = await Contact.findById(req.params.id);
  res.render("show-contact", { contact });
};

module.exports.deleteContact = async (req, res) => {
  try {
    const contact = await Contact.findByIdAndDelete(req.params.id);
    res.redirect("/");
  } catch (error) {
    console.error("Error deleting contact:", error);
    res.redirect("/"); // Redirect even on error to prevent the app from crashing
  }
};

module.exports.addContact = async (req, res) => {
  const contact = await Contact.create(req.body);
  res.redirect("/");
};

module.exports.updateContact = async (req, res) => {
  try {
    console.log("Update contact called with ID:", req.params.id);
    console.log("Request body:", req.body);
    console.log("Request method:", req.method);

    const contact = await Contact.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    });
    console.log("Contact updated successfully:", contact);
    res.redirect("/");
  } catch (error) {
    console.error("Error updating contact:", error);
    res.redirect("/");
  }
};

module.exports.getContactById = async (req, res) => {
  const contact = await Contact.findById(req.params.id);
  res.render("update-contact", { contact });
};
