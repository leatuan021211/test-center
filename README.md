# Test Center

Framwork Excercise

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)

## Project Overview

This project is a web appication with API Service built using Django and Django REST Framework. It provides Admin sites, Random Question Test, Authorization using JWT. 

## Features

- User authentication and authorization
- RESTful API endpoints for CRUD operations
- User Management
- Test Management
- Assignment Management
- Question Management

## Requirements

- Python 3.11
- Django
- Django REST Framework
- djangorestframework simplejwt
- drf-yasg

## Installation

1. **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/yourprojectname.git](https://github.com/leatuan021211/test-center.git)
    cd test-center
    ```

2. **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (for accessing the admin panel):**
    ```bash
    python manage.py createsuperuser
    ```

## Usage

1. **Start the development server:**
    ```bash
    python manage.py runserver
    ```

2. Access the application at `http://127.0.0.1:8000`.

## API Documentation

The API follows RESTful principles and provides the following endpoints:

| Method | Endpoint                                  | Description                       |
| ------ | ----------------------------------------- | --------------------------------- |
|        | `/admin/`                                 | Go to Admin Site                  |
|        | `/swagger/`                               | Go to Swagger                     |
| POST   | `/api/v1/auth/login/`                     | Login                             |
| POST   | `/api/v1/auth/refresh/`                   | Refresh Token                     |
| DELETE | `/api/v1/auth/logout/`                    | Logout                            |
| DELETE | `/api/v1/auth/logout/all/`                | Logout all location               |
| GET    | `/api/v1/assignments/`                    | List all assignments              |
| GET    | `/api/v1/users/profile/`                  | Retrieve User Information         |
| GET    | `/api/v1/assignments/<id>/`               | Retrieve a specific assignment    |
| GET    | `/api/v1/assignments/<id>/questions`      | List all questions of assignment  |
| POST   | `/api/v1/assignments/submission/`         | Submit an assignment              |
