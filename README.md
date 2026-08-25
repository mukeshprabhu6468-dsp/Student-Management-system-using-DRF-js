Student Management Using Django REST Framework:

A Student Management System built using Python, Django, Django REST Framework (DRF), JWT Authentication, and a frontend interface.

This project provides REST APIs to manage student records and includes authentication to protect the API endpoints.

📌 Project Overview:

The Student Management System allows users to manage student information through REST APIs.

The system supports:

->User authentication
->JWT access and refresh tokens
->Add new students
->View all students
->View individual student details
->Edit student information
->Delete student records
->Frontend interface for interacting with the APIs
->Database storage using SQLite


🚀 Features:

* Student Management
  ->Create a new student
  ->Display all students
  ->View a particular student
  ->Update student details
  ->Delete a student

* Authentication
The project uses JWT (JSON Web Token) authentication.
It provides:
 ->Login
 ->Access token
 ->Refresh token
 ->Protected API endpoints
The access token is used to authenticate API requests.

🛠️ Technologies Used:

Backend

  ->Python
  ->Django
  ->Django REST Framework
  ->Simple JWT

Frontend

  ->HTML
  ->CSS
  ->JavaScript
  ->Bootstrap

Database

  ->SQLite

Development Tools

  ->Visual Studio Code
  ->Git
  ->GitHub
  ->Postman


📂 Project Structure:

Student Management Using DRF/
│
├── Frontend/
│   └── Frontend files
│
├── JWTAuthentication/
│   └── JWT authentication related files
│
├── student_app/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── student_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── .gitignore
├── manage.py
└── README.md


⚙️ Installation:

1. Clone the repository

git clone https://github.com/YOUR-USERNAME/student-management-drf.git


2. Open the project

cd student-management-drf


3. Create a virtual environment

=>python -m venv .venv


4. Activate the virtual environment

Windows
=>.venv\Scripts\activate


5. Install dependencies

If the project contains a requirements.txt file:

=>pip install -r requirements.txt

Otherwise, install the required packages:

=>pip install django
=>pip install djangorestframework
=>pip install djangorestframework-simplejwt
=>pip install django-cors-headers


🗄️ Database Setup

Run the migrations:

=>python manage.py makemigrations
=>python manage.py migrate

▶️ Run the Project:

Start the Django development server:

=>python manage.py runserver

The backend will normally be available at:

=>http://127.0.0.1:8000/

Open this address in your browser.

🔐 JWT Authentication:

The authentication system uses JWT tokens.

Login

Send the user's username and password to the login endpoint.

Example:

=>POST /api/token/

Request:

{
    "username": "your_username",
    "password": "your_password"
}

The server returns:

{
    "access": "access_token",
    "refresh": "refresh_token"
}


Using the Access Token:

For protected API requests, add the token to the request header:

Authorization: Bearer <access_token>

Refresh Token:

When the access token expires, use the refresh token to obtain a new access token.

=>POST /api/token/refresh/

Example:

{
    "refresh": "your_refresh_token"
}


🔗 Student API Operations:

The API provides CRUD operations for student records.

Operation	        Method	      Purpose
Create Student	  POST	        Add a new student
Get Students	    GET	          Display all students
Get Student	      GET	          Display one student
Update Student	  PUT/PATCH	    Edit student information
Delete Student	  DELETE	      Remove a student


🧪 Testing the APIs:

You can test the APIs using Postman.

For protected endpoints:

 1. Login and obtain the JWT access token.
 2. Open the API request in Postman.
 3. Go to Authorization.
 4. Select Bearer Token.
 5. Enter the access token.
 6. Send the request.


🖥️ Frontend:

The project also contains a frontend interface that communicates with the Django REST APIs.

The frontend can be used to:

 * Display students
 * Add students
 * Edit students
 * Delete students
 * Interact with the backend API


🔒 Security:

The following files and folders are excluded from Git using .gitignore:

 * Virtual environment
 * SQLite database
 * Python cache files
 * Environment variables
 * VS Code configuration

Sensitive information such as passwords, secret keys, and database credentials should not be uploaded to GitHub.

🎯 Future Improvements:

Possible improvements include:

Student search
Pagination
Student profile pages
Role-based authentication
Admin dashboard
PostgreSQL/MySQL database
API documentation using Swagger/OpenAPI


👨‍💻 Author:
MUKESH S.,
Python Full Stack Developer

📄 License

This project is created for learning and development purposes.
