import express from "express";
import contactController from "../controllers/contactController.js";

const router = express.Router();



// Render Routes

router.get("/", contactController.homePage);
router.get("/add-contact", contactController.addContactPage);
router.get("/show-contact/:id", contactController.getContactById);
router.get("/update-contact/:id", contactController.updateContactPage);
router.get("/delete-contact/:id", contactController.deleteContact);


// add contact
router.post("/add-contact", contactController.addContact);
// update contact
router.post("/update-contact/:id", contactController.updateContact);


// delete contact




























export default router;