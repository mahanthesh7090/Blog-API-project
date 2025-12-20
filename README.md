A RESTful Blog Application API built using Django Rest Framework (DRF) that allows users to register, authenticate using JWT, and perform CRUD operations on blog posts and comments.
This project was developed as part of an internship full-stack / backend development project.

All API endpoints are documented using Postman.
The collection includes request/response examples, authentication headers,
and error cases.

Project Structure
blog/
│
├── app/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   ├── urls.py
│   └── tests/
│       ├── test_post_api.py
│       ├── test_comment_api.py
│       ├── test_serializers.py
│       ├── test_models.py
│       └── test_permissions.py
│
├── blog/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── docs/
│   └── postman/
│       └── Blog_API_Documentation.postman_collection.json
│
├── manage.py
└── README.md

Installation & Setup

1️Clone the Repository
git clone https://github.com/your-username/blog-rest-api.git
cd blog-rest-api

Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

Install Dependencies
pip install -r requirements.txt

Run Migrations
python manage.py makemigrations
python manage.py migrate

Create Superuser (Optional)
python manage.py createsuperuser

Run the Server
python manage.py runserver


Server will start at:

http://127.0.0.1:8000/

esting
Run All Tests
python manage.py test

Testing Types Implemented

Unit Tests
Integration Tests
  






