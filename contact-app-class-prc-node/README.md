# Contact Management App

A full-stack web application for managing contacts built with Node.js, Express, MongoDB, and EJS templating engine.

## 🚀 Features

- **CRUD Operations**: Create, Read, Update, and Delete contacts
- **Modern UI**: Clean and responsive design using Bootstrap
- **Real-time Database**: MongoDB integration with Mongoose ODM
- **Server-side Rendering**: EJS templating for dynamic content
- **RESTful API**: Well-structured routes and controllers
- **Environment Configuration**: Secure configuration management

## 📋 Prerequisites

Before running this application, make sure you have the following installed:

- **Node.js** (v18 or higher)
- **npm** (Node Package Manager)
- **MongoDB** (or Docker for containerized setup)
- **Git** (for cloning the repository)

## 🛠️ Installation

### Option 1: Local Setup

1. **Clone the repository**

   ```bash
   git clone <your-repository-url>
   cd contact-app-class-prc-node
   ```

2. **Install dependencies**

   ```bash
   npm install
   ```

3. **Set up environment variables**

   ```bash
   cp config.env.example config.env
   ```

   Edit `config.env` with your configuration:

   ```env
   DATABASE_URL=mongodb://localhost:27017/contact_app
   PORT=7000
   ```

4. **Start MongoDB** (if running locally)

   ```bash
   # Ubuntu/Debian
   sudo systemctl start mongod

   # macOS (if installed via Homebrew)
   brew services start mongodb-community

   # Windows
   net start MongoDB
   ```

5. **Run the application**
   ```bash
   npm start
   ```

### Option 2: Docker Setup (Recommended)

1. **Clone the repository**

   ```bash
   git clone <your-repository-url>
   cd contact-app-class-prc-node
   ```

2. **Create docker-compose.yml**

   ```yaml
   version: "3.8"
   services:
     mongodb:
       image: mongo:latest
       container_name: mongodb-container
       restart: always
       ports:
         - "27017:27017"
       environment:
         MONGO_INITDB_ROOT_USERNAME: uzair
         MONGO_INITDB_ROOT_PASSWORD: uzairyasin123
       volumes:
         - mongo_data:/data/db
       networks:
         - node-app-network

     app:
       build: .
       container_name: contact-app
       restart: always
       ports:
         - "7000:7000"
       environment:
         - DATABASE_URL=mongodb://uzair:uzairyasin123@mongodb-container:27017/my_database?authSource=admin
         - PORT=7000
       depends_on:
         - mongodb
       networks:
         - node-app-network

   volumes:
     mongo_data:

   networks:
     node-app-network:
       driver: bridge
   ```

3. **Run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

## 📁 Project Structure

```
contact-app-class-prc-node/
├── app.js                 # Express app configuration
├── server.js              # Server entry point
├── database.js            # MongoDB connection
├── config.env             # Environment variables
├── package.json           # Dependencies and scripts
├── Dockerfile             # Docker configuration
├── controllers/
│   └── contactController.js  # Contact CRUD operations
├── models/
│   └── contactModel.js    # Mongoose contact schema
├── routes/
│   └── contactRoutes.js   # Contact routes
├── views/
│   ├── index.ejs          # Home page
│   ├── add-contact.ejs    # Add contact form
│   ├── show-contact.ejs   # Contact details
│   ├── update-contact.ejs # Edit contact form
│   └── partials/
│       ├── header.ejs     # Header template
│       └── footer.ejs     # Footer template
└── public/
    ├── bootstrap.min.css  # Bootstrap styles
    └── custom.css         # Custom styles
```

## 🎯 Usage

Once the application is running:

1. **Access the application**: Open your browser and go to `http://localhost:7000`

2. **Add a new contact**: Click "Add Contact" and fill in the form

   - Name (required)
   - Email (required)
   - Phone number
   - Address

3. **View contacts**: All contacts are displayed on the home page

4. **Edit contact**: Click "Edit" on any contact to modify details

5. **Delete contact**: Click "Delete" to remove a contact

6. **View contact details**: Click on a contact name to see full details

## 🔧 Available Scripts

- `npm start` - Start the production server
- `npm run dev` - Start the development server with nodemon (if configured)
- `npm test` - Run tests (if configured)

## 🗄️ Database Schema

The Contact model includes:

- **name** (String, required)
- **email** (String, required, unique)
- **phone** (String)
- **address** (String)
- **createdAt** (Date, auto-generated)
- **updatedAt** (Date, auto-updated)

## 🌐 API Endpoints

- `GET /` - Display all contacts
- `GET /add` - Show add contact form
- `POST /add` - Create new contact
- `GET /contact/:id` - Show contact details
- `GET /contact/:id/edit` - Show edit form
- `PUT /contact/:id` - Update contact
- `DELETE /contact/:id` - Delete contact

## 🔒 Environment Variables

Create a `config.env` file in the root directory:

```env
DATABASE_URL=mongodb://username:password@localhost:27017/database_name
PORT=7000
```

## 🐳 Docker Commands

```bash
# Build the image
docker build -t contact-app .

# Run the container
docker run -p 7000:7000 --env-file config.env contact-app

# Run with Docker Compose
docker-compose up --build

# Stop containers
docker-compose down

# View logs
docker-compose logs -f
```

## 🚨 Troubleshooting

### Common Issues

1. **MongoDB Connection Error**

   - Ensure MongoDB is running
   - Check your connection string in `config.env`
   - Verify network connectivity

2. **Port Already in Use**

   - Change the PORT in `config.env`
   - Kill the process using the port: `lsof -ti:7000 | xargs kill -9`

3. **Docker Issues**
   - Ensure Docker is running
   - Check container logs: `docker logs container-name`
   - Rebuild images: `docker-compose build --no-cache`

### Development Tips

- Use `nodemon` for automatic server restart during development
- Check browser console for client-side errors
- Monitor server logs for backend issues
- Use MongoDB Compass for database visualization

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the ISC License.

## 👨‍💻 Author

Created by [Your Name]

## 📞 Support

For support and questions, please open an issue in the repository.
