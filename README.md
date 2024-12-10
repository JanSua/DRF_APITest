
# Django REST Framework Tasks API

This repository contains a simple example of a Django REST Framework (DRF) project. It provides a basic RESTful API for a task management system with CRUD functionality.

## 🚀 **Getting Started**

### **1. Clone the Repository**
First, clone the repository to your local machine:

```bash
git clone https://github.com/JanSua/DRF_APITest.git
```

### **2. Navigate to the Project Directory**
```bash
cd DRF_APITest
```

### **3. Set Up a Virtual Environment (Optional but Recommended)**

#### Using `venv`:
```bash
python -m venv venv
source venv/bin/activate  # For Windows use `venv\Scripts\activate`
```

### **4. Install Dependencies**
Install the necessary dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## 🛠️ **Running the Application**

### **Apply Migrations**
Before running the server, apply the migrations:
```bash
python manage.py migrate
```

### **Start the Development Server**
```bash
python manage.py runserver
```

The application should now be running at [http://localhost:8000](http://localhost:8000).

## 🧪 **Testing the Endpoints**

### **Base URL**
The base URL for the API is:
```plaintext
http://localhost:8000/api/
```

### **Available Endpoints**
Here are the endpoints available:

- **GET `/tasks/`** - List all tasks.
- **POST `/tasks/`** - Create a new task.
- **GET `/tasks/<task_id>/`** - Retrieve a single task by ID.
- **PUT `/tasks/<task_id>/`** - Update a task by ID.
- **DELETE `/tasks/<task_id>/`** - Delete a task by ID.

You can use tools like [Postman](https://www.postman.com/) or cURL to test these endpoints.

## 📄 **Technologies Used**
- **Django 4.x.x**
- **Django REST Framework 3.x.x**

## 📌 **Notes**
- Database used: SQLite (default Django database).
- The application is ready for local development only.
- If deploying to production, consider using a production-ready database and server configuration.

## 📢 **Contributing**
Feel free to fork, submit issues, or suggest features.
