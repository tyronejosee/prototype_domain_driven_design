# **Prototype Domain-driven Design**

This project is an implementation of a web application based on Django and Django REST Framework following the principles of Domain-Driven Design (DDD). The project's architecture is designed to maintain a clear separation between the different domain components, ensuring scalability, maintainability, and testability.

## 📂 **Project Structure**

The project follows a DDD-based structure:

```bash
project_root/
|-- config/                   # Global configurations
|-- apps/
|   |-- __init__.py           # Application initialization
|   |-- <app>/
|       |-- domain/           # Domain logic (Entities, Value Objects, Repositories)
|       |-- application/      # Use cases and application services
|       |-- infrastructure/   # Concrete implementations (ORM, APIs, Serializers)
|       |-- presentation/     # Views and endpoints
|-- shared/                   # Shared logic
|-- tests/                    # Unit and integration tests
|-- manage.py
|-- requirements.txt          # Dependencies with pip (alternative to Poetry)
|-- README.md
```

## 🛠️ **Installation and Configuration**

- Clone the repository

```bash
git clone https://github.com/user/django-ddd-project.git
cd django-ddd-project
```

- Create and activate a virtual environment

```sh
python -m venv venv

# On Linux-Mac
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

- Install dependencies

```bash
pip install -r requirements.txt
```

- Set up environment variables

Copy `.env.example`, rename it to `.env`, and configure your own environment variables.

```sh
SECRET_KEY=your_secret_here
DEBUG=True
...
```

- Apply migrations and run the server

```sh
python manage.py migrate
python manage.py runserver
```

## 🚀 **Usage**

The project exposes a REST API at `http://127.0.0.1:8000/api/`. You can test it using tools like Postman or curl.

```bash
curl http://127.0.0.1:8000/api/products/
```

## 🧪 **Testing**

- Run tests

```bash
pytest
```

## ⚖️ **License**

This project is licensed under the MIT License. See the `LICENSE` file for more details.
