







// RENDER CONTROLERS
const homePage = (req, res) => {
    res.render("index");
}


const addContactPage = (req, res) => {
    res.render("add-contact");
}


const showContactPage = (req, res) => {
    res.render("show-contact");
}

const updateContactPage = (req, res) => {
    res.render("update-contact");
}




export default { homePage, addContactPage, showContactPage, updateContactPage };


