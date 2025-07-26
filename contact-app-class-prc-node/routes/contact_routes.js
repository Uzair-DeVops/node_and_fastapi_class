import express from "express";
import contactController from "../controllers/contact_controller.js";

const router = express.Router();



// Render Routes

router.get("/", contactController.homePage);
router.get("/add-contact", contactController.addContactPage);
router.get("/show-contact", contactController.showContactPage);
router.get("/update-contact", contactController.updateContactPage);





































export default router;