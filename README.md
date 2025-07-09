# 🛠️ Django & Docker Projects Repository

Welcome to my collection of Django projects and mini-projects, containerized using Docker for consistency, scalability, and ease of deployment. This repository showcases both full-stack applications and smaller utilities built as part of my learning journey and contributions to real-world problems.


## 📁 Repository Structure

```

django-docker-projects/
│
├── project-name-1/
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── manage.py
│   └── app/
│
├── mini-project-1/
│   ├── docker-compose.yml
│   ├── Dockerfile
│   └── ...
│
└── README.md

````

<br>

## 🧰 Tech Stack

- **Backend Framework:** [Django](https://www.djangoproject.com/)
- **Containerization:** [Docker](https://www.docker.com/)
- **Database:** PostgreSQL / SQLite (project-specific)
- **Frontend (if applicable):** HTML, CSS, JavaScript, Bootstrap
- **Dev Tools:** Git, VS Code, Docker Compose

<br>

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose
- Git

<br>

### Clone the Repository

```bash
git clone https://github.com/<your-username>/django-docker-projects.git
cd django-docker-projects
````

<br>

### Running a Project

Navigate to a project folder and use Docker Compose to build and run:

```bash
cd project-name-1
docker-compose up --build
```

Your Django app will be available at `http://localhost:8000`.

<br>

## 🧪 Example Projects

### 🔹 Project: Blog App

A simple blogging platform with authentication, CRUD posts, and comments.

* `/blog-app`
* Features: User registration, post editor, comment system
* Dockerized with PostgreSQL

### 🔹 Mini Project: Task Tracker

* `/task-tracker-mini`
* A lightweight task manager with Django admin
* Uses SQLite for storage

<br>

## 🗃️ Additional Notes

* All environments are isolated via Docker.
* Database credentials and environment settings can be found in `.env.example`.
* Admin credentials are usually set to:

  * **Username:** `admin`
  * **Password:** `admin123`

<br>

## 🎯 Future Improvements

* Add CI/CD pipeline with GitHub Actions
* Migrate projects to PostgreSQL (if using SQLite)
* Add NGINX + Gunicorn for production-ready setup

<br>

## 📬 Contact

Feel free to connect with me on:

* 🌐 [LinkedIn](https://www.linkedin.com/in/marknature-c/)

<br>

## 📄 License

This repository is open-source and available under the [MIT License](LICENSE).
