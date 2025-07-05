**Live address:** [https://django-rest-api-project.onrender.com](https://django-rest-api-project.onrender.com)  
**Documentation:** [Swagger UI](https://django-rest-api-project.onrender.com/docs/) | 
                   [Redoc](https://django-rest-api-project.onrender.com/redoc/)
**Github repo:** [github](https://github.com/SergeiLisitsyn/django-rest-api-project) 
---


## 🚀 Project Overview

This is a **Django REST Framework**–powered API designed to manage IT projects and their associated vacancies.
It supports full CRUD operations, nested relationships, and interactive documentation via Swagger and Redoc. 
The backend is deployed on **Render.com**, using an internal PostgreSQL service for data persistence.

---

## 📦 Core Features

- **Projects Module**  
  Each project includes metadata such as name, field, experience level, description, and deadline.

  - Validation for all fields except deadline is handled by the default Django REST Framework mechanisms.
  A custom validation has been implemented specifically for the deadline field:
    The deadline cannot be earlier than 24 hours after the project’s creation time.

- **Vacancies Module**  
  Vacancies are linked to specific projects via foreign key relationships. Each vacancy contains a description 
- and inherits its project context.

- **Nested Endpoints**  
  Vacancies are accessed through their parent project, ensuring logical data grouping and clean URL structure.

- **Interactive API Docs**  
  Swagger UI (`/docs/`) and Redoc (`/redoc/`) provide live documentation and testing interfaces.

- **Admin Panel**  
  Django Admin is enabled for managing projects and vacancies via a web interface.
  To login https://django-rest-api-project.onrender.com/admin/  use - user: alex, password: alexpass
---

## 🔌 API Endpoints

### Projects

| Method | Endpoint                     | Description                      |
|--------|------------------------------|----------------------------------|
| GET    | `/projects/`                 | List all projects                |
| POST   | `/projects/`                 | Create a new project             |
| GET    | `/projects/{id}/`            | Retrieve a specific project      |
| PUT    | `/projects/{id}/`            | Update a project                 |
| DELETE | `/projects/{id}/`            | Delete a project                 |

### Vacancies (Nested under Projects)

| Method | Endpoint                                 | Description                       |
|--------|------------------------------------------|-----------------------------------|
| GET    | `/projects/{id}/vacancies/`              | List vacancies for a project      |
| POST   | `/projects/{id}/vacancies/`              | Create a vacancy under a project  |
| GET    | `/projects/{id}/vacancies/{vacancy_id}/` | Retrieve a specific vacancy    or |
| GET    | ` /vacancies/{vacancy_id}/`              | Retrieve a specific vacancy       |
| PUT    | `/projects/{id}/vacancies/{vacancy_id}/` | Update a vacancy               or |
| PUT    | ` /vacancies/{vacancy_id}/`              | Update a vacancy                  |
| DELETE | `/projects/{id}/vacancies/{vacancy_id}/` | Delete a vacancy              or  |
| DELETE | ` /vacancies/{vacancy_id}/`              | Delete a vacancy                  |

> Note: The endpoint `/vacancies/` returns no data because vacancies are scoped to their parent project.

---

## 🛠 Technologies Used

| Layer        | Stack                                    |
|--------------|------------------------------------------|
| Backend      | Django 5.2.3, Django REST Framework      |
| Database     | PostgreSQL (via Render internal service) |
| Deployment   | Render.com                               |
| Docs         | drf-yasg (Swagger, Redoc)                |
| Static Files | WhiteNoise                               |

---

## ⚙️ Configuration Highlights

- `drf_yasg` is used for schema generation and UI rendering.
- Static files are served via WhiteNoise.
- `collectstatic` is run during deployment to gather Swagger assets.
- Permissions are set to `AllowAny` for public API access.
- Admin interface is customized with `list_display`, `search_fields`, and `list_filter`.

---

## 🧪 Testing & Interaction

- Use Swagger UI at [`/docs/`](https://django-rest-api-project.onrender.com/docs/) to test endpoints.
- Use `curl` or Postman for direct API interaction:
- examples:
```bash
DELETE
curl -X DELETE https://django-rest-api-project.onrender.com/projects/1/vacancies/2/
PUT
curl -X PUT https://django-rest-api-project.onrender.com/projects/3/      -H "Content-Type: application/json"      -d '{
           "id": 3,
           "name": "Update",
           "field": "Edit / Update",
           "experience": "Edit",
           "description": "Update",
           "deadline": "2026-12-31T23:00:00Z"
         }'
```

---

## 🧠 Example Use Case

This API could power a job board or internal project tracker where each IT project has its own set of open roles. 
It’s ideal for integrating with frontend frameworks or mobile apps.
