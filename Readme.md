# User Preferences Dashboard

**Django Backend**

![Django](https://img.shields.io/badge/Backend-Django-green)
![REST API](https://img.shields.io/badge/API-REST-orange)

A modern **full-stack user preferences management system** built with **Webix UI (Frontend)** and **Django REST API (Backend)**.

---

## Features

* RESTful API
* Secure Data Storage
* Django Admin Panel
* CORS Enabled for Frontend Integration
* SQLite Database (Default)

---

# 📁 Project Structure

```
Backend-CaseStudy/
│
├── manage.py
├── backend/
│   └── settings.py
├── settings_app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── db.sqlite3
├── requirements.txt
└── README.md
```

---

# Backend Setup (Django)

### 1. Open backend folder

```bash
cd Backend-CaseStudy
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create superuser

```bash
python manage.py createsuperuser
```

### 6. Run server

```bash
python manage.py runserver
```

Backend will run at:

```
http://127.0.0.1:8000
```

---

# 🔐 Django Admin Panel

Login at:

```
http://127.0.0.1:8000/admin/
```

View:

* Saved User Accounts
* Settings Records
* API Data

---

# 🔌 API Endpoints

| Method | Endpoint        | Description           |
| ------ | --------------- | --------------------- |
| POST   | `/api/account/` | Save account settings |
| GET    | `/api/account/` | Retrieve saved data   |

---
