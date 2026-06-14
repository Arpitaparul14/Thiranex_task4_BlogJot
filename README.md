# 📝 BlogJot — Modern Django Blog Platform

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge\&logo=python)
![Django](https://img.shields.io/badge/Django-4.x-green?style=for-the-badge\&logo=django)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)

A feature-rich blogging platform built with Django that enables users to create, manage, and interact with blog content through comments, likes, notifications, and category-based organization.

Developed as part of the **Thiranex Internship Program**.

---

## 🌟 Overview

BlogJot is a complete blogging solution designed to provide an engaging writing and reading experience. Users can publish articles, upload images, organize content through categories, interact via comments and likes, and receive notifications for activity on their posts.

The platform features a modern purple-themed user interface, responsive design, and a powerful Django backend for content management.

---

## ✨ Key Features

### 🔐 Authentication System

* User Registration
* Secure Login & Logout
* User-specific content management

### 📝 Blog Management

* Create blog posts
* Edit existing posts
* Delete posts
* Upload featured images

### 🗂️ Category Support

* Organize posts into categories
* Browse content by category

### 💬 Interactive Community

* Comment on blog posts
* View discussions
* Increase user engagement

### ❤️ Like System

* Like and unlike posts
* Track user interactions

### 🔔 Notification System

* Notifications for new comments
* Notifications for likes
* Real-time engagement updates

### 📚 Personal Dashboard

* View all authored posts
* Manage published content

### 🎨 Modern UI

* Clean and responsive design
* Purple & white theme
* Poppins typography
* Font Awesome icons

### ⚙️ Admin Dashboard

* Manage users
* Manage posts
* Manage comments
* Manage categories
* Manage notifications

---

## 🛠️ Tech Stack

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python 3.12  | Programming Language |
| Django 4.x   | Backend Framework    |
| SQLite       | Database             |
| HTML5        | Structure            |
| CSS3         | Styling              |
| Font Awesome | Icons                |
| Google Fonts | Typography           |

---

## 📂 Project Structure

```bash
blogjot/
│
├── blog/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
│
├── blogjot/
│   ├── settings.py
│   ├── urls.py
│   └── context_processors.py
│
├── templates/
├── static/
├── media/
├── manage.py
└── README.md
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Arpitaparul14/Thiranex_task4_BlogJot.git
cd Thiranex_task4_BlogJot
```

### 2️⃣ Install Dependencies

```bash
pip install django pillow
```

### 3️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4️⃣ Create Admin Account

```bash
python manage.py createsuperuser
```

### 5️⃣ Start Development Server

```bash
python manage.py runserver
```

### 6️⃣ Visit the Application

```text
http://127.0.0.1:8000/
```

---

## 📸 Application Pages

| Feature       | Route             |
| ------------- | ----------------- |
| Home          | `/`               |
| Create Post   | `/post/create/`   |
| My Posts      | `/my-posts/`      |
| Notifications | `/notifications/` |
| Login         | `/login/`         |
| Register      | `/register/`      |
| Admin Panel   | `/admin/`         |

---

## 🎯 Learning Outcomes

This project demonstrates practical implementation of:

* Django Authentication
* CRUD Operations
* Model Relationships
* Django Forms
* File Upload Handling
* User Notifications
* Database Management
* Template Inheritance
* Responsive UI Design

---

## 📌 Future Enhancements

* Rich Text Editor
* Search Functionality
* User Profiles
* Follow System
* Bookmark Posts
* Dark Mode
* Email Notifications
* REST API Integration

---

## 👩‍💻 Developer

### Arpita Parul

🔗 GitHub: https://github.com/Arpitaparul14

🎓 Internship Project: Thiranex Internship Program

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

Your support motivates further development and improvements.
