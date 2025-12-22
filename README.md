# Blog REST API – Internship Project

A **RESTful Blog Application API** built using **Django Rest Framework (DRF)** that allows users to register, authenticate using **JWT**, and perform **CRUD operations** on blog posts and comments.

This project was developed as part of an **internship**.

All project guidelines are available in a **PDF document** located in the `docs` folder.

---

##  Quick Setup – Installation Guide

### 1. Create Virtual Environment
```
## python -m venv venv
## source venv/bin/activate   # Windows: venv\Scripts\activate
```
### 2. Install Dependencies
```
pip install -r requirements.txt
```
### 3 Configure PostgreSQL Database

Create a PostgreSQL database named blog and update the following details in blog/settings.py under the DATABASES section:

Database name :

Username:

Password:

Host:

Port:

### 4️. Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```
### 5️. Run the Server
```
python manage.py runserver
```

### The server will start at:

```
http://127.0.0.1:8000/
```
### ✅ Notes

Make sure PostgreSQL is running before starting the server

Use Postman or any API client to test the endpoints

JWT authentication is required for protected routes
