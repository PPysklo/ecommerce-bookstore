# Bookstore Project

## Overview

This is a Django-based bookstore application that allows users to browse, search, and purchase books. The application includes features such as user authentication, shopping cart, order processing, and stock management.

## Features

- User authentication (login, registration, logout) and profile management
- Shopping cart functionality
- Order processing with stock validation
- Admin panel for managing books, orders, and users
- Browse books by categories and tags
- Search for books
- Order confirmation and status update emails

# Getting Started with Bookstore

Follow these steps to set up and run the Bookstore application:

## 1. Clone the Repository
```sh
git clone https://github.com/yourusername/bookstore.git
cd bookstore
```

## 2. Set Up a Virtual Environment
Create and activate a virtual environment to isolate the project's dependencies:
```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

## 3. Install Dependencies
Install the required packages:
```sh
pip install -r requirements.txt
```

## 4. Apply Migrations
Set up the database by applying migrations:
```sh
python manage.py makemigrations
python manage.py migrate
```

## 5. Create a Superuser
Create a superuser account to access the admin panel:
```sh
python manage.py createsuperuser
```

## 6. Start the Development Server
Run the development server:
```sh
python manage.py runserver
```

## 7. Access the Application
Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the application.

---

# Project Structure
The project is organized as follows:

- bookstore: Contains the main application code.

- templates/: Stores HTML templates for the frontend.

- static/: Includes static files like CSS, JavaScript, and images.

- css/: Contains CSS files for styling.

- js/: Contains JavaScript files for interactivity.

- requirements.txt: Lists the Python dependencies for the project.

- manage.py: The Django project's management script.

```sh
bookstore/
├── .gitignore
├── db.sqlite3
├── email_secrets.py
├── manage.py
├── README.md
├── requirements.txt
├── __pycache__/
│   ├── email_secrets.cpython-310.pyc
│   ├── secrets.cpython-310.pyc
├── app_books/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── models.py
│   ├── signals.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   ├── views.py
│   ├── __pycache__/
│   ├── migrations/
│   ├── templates/
│   │   ├── app_books/
│   │   │   ├── books_list.html
│   │   │   ├── shopping_cart.html
│   │   │   ├── checkout.html
│   │   │   ├── order_confirmation_email.html
│   │   │   ├── order_status_update_email.html
│   │   │   ├── welcome_email.html
├── app_users/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── signals.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── __pycache__/
│   ├── migrations/
│   ├── templates/
│   │   ├── app_users/
│   │   │   ├── login_register.html
│   │   │   ├── profile.html
│   │   │   ├── profile_edit.html
├── bookstore/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── media/
├── static/
│   ├── css/
│   │   ├── cart.css
│   │   ├── footer.css
│   │   ├── login_register.css
│   │   ├── main_style.css
│   │   ├── navbar_style.css
│   │   ├── paginations.css
│   │   ├── profile_edit.css
│   ├── js/
│   │   ├── cart.js
│   │   ├── footer_script.js
│   │   ├── login_register.js
│   │   ├── navbar_scripts.js 
├── templates/
│   ├── base.html
│   ├── footer.html
│   ├── index.html
│   ├── navbar.html
│   ├── pagination.html
│   ├──reset_password_complete.html
│   ├──reset_password_sent.html
│   ├──reset_password.html
│   ├──reset.html
│   ├──shooping_cart.html
│   ├──statute.html
├── manage.py
├── requirements.txt
```