import Contact from "../models/contactModel.js";







// RENDER CONTROLERS
const homePage = async (req, res) => {
        const data = await Contact.find();
        res.render("index", { data });
}
const addContactPage = (req, res) => {
    res.render("add-contact");
}

const updateContactPage = async (req, res) => {
    const contact = await Contact.findById(req.params.id);
    res.render("update-contact", { contact });
}

const getContactById = async (req, res) => {
  const contact = await Contact.findById(req.params.id);
  res.render("show-contact", { contact });
};



// REDIRECT CONTROLERS
const addContact = async (req, res) => {
  const data = req.body;
  const contact = await Contact.create(data);
  res.redirect("/");
};
const updateContact = async (req, res) => {
    const data = req.body;
    const contact = await Contact.findByIdAndUpdate(req.params.id, data, { new: true });
    res.redirect("/");
}

const deleteContact = async (req, res) => {
    const contact = await Contact.findByIdAndDelete(req.params.id);
    res.redirect("/");
}


export default { 
    homePage,
    addContactPage,
    updateContactPage, 
    addContact, 
    getContactById, 
    updateContact , 
    deleteContact };


