import app from "./app.js";









app.listen(process.env.PORT, () => {
    console.log(`Server is running on url http://localhost:${process.env.PORT}`);
});