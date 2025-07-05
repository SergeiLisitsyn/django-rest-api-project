
# 🚀 Обзор проекта SmartCareer & CloudTask API

**Живой адрес:** [https://django-rest-api-project.onrender.com](https://django-rest-api-project.onrender.com)  
**Документация:** [Swagger UI](https://django-rest-api-project.onrender.com/docs/) | 
                   [Redoc](https://django-rest-api-project.onrender.com/redoc/)
**Github репозиторий:** [github](https://github.com/SergeiLisitsyn/django-rest-api-project) 
---

## 📦 Описание

Это API, построенное на **Django REST Framework**, предназначено для управления IT-проектами и связанными с ними 
вакансиями. Оно поддерживает полные операции CRUD, вложенные маршруты и интерактивную документацию.

Бэкенд размещён на платформе **Render**, с использованием внутреннего сервиса **PostgreSQL**.

---

## 🧠 Основные возможности

- 🔹 **Модуль проектов**  
  Каждый проект содержит поля: name, field, experience level, description, and deadline.
- Валидация всех полей за исключением deadline реализована дефолтная Django REST Framework. Для поля deadline создана
- кастомная валидация: deadline не может быть раньше чем через сутки от времени создания проекта. 

- 🔹 **Модуль вакансий**  
  Вакансии связаны с конкретными проектами через `ForeignKey`. Каждая вакансия содержит описание (description) 
- и наследует имя (name) проекта.

- 🔹 **Вложенные эндпоинты**  
  Вакансии доступны только через родительский проект, что обеспечивает логичную структуру URL.

- 🔹 **Swagger и Redoc**  
  Интерактивная документация по API позволяет тестировать запросы в браузере.

- 🔹 **Панель администратора Django**  
  Удобный интерфейс для управления проектами и вакансиями вручную.
  Для входа в https://django-rest-api-project.onrender.com/admin/  используйте user: alex, password: alexpass
---

## 🔌 Эндпоинты API

### Проекты

| Метод  | Эндпоинт            | Описание                    |
|--------|---------------------|-----------------------------|
| GET    | `/projects/`        | Список всех проектов        |
| POST   | `/projects/`        | Создание нового проекта     |
| GET    | `/projects/{id}/`   | Получение проекта по ID     |
| PUT    | `/projects/{id}/`   | Обновление проекта          |
| DELETE | `/projects/{id}/`   | Удаление проекта            |

### Вакансии (вложенные в проекты)

| Метод  | Эндпоинт                                 | Описание                        |
|--------|------------------------------------------|---------------------------------|
| GET    | `/projects/{id}/vacancies/`              | Список вакансий проекта         |
| POST   | `/projects/{id}/vacancies/`              | Добавление вакансии в проект    |
| GET    | `/projects/{id}/vacancies/{vacancy_id}/` | Получение вакансии по ID    или |
| GET    | ` /vacancies/{vacancy_id}/`              | Получение вакансии по ID        |
| PUT    | `/projects/{id}/vacancies/{vacancy_id}/` | Обновление вакансии         или |
| PUT    | ` /vacancies/{vacancy_id}/`              | Обновление вакансии             |
| DELETE | `/projects/{id}/vacancies/{vacancy_id}/` | Удаление вакансии           или |
| DELETE | ` /vacancies/{vacancy_id}/`              | Удаление вакансии               |

> 💡 Эндпоинт `/vacancies/` не используется, так как каждая вакансия привязана к проекту.

---

## ⚙️ Технологии

| Уровень      | Технология                          |
|--------------|-------------------------------------|
| Бэкенд       | Django 5.2.3, DRF                   |
| База данных  | PostgreSQL (Render Internal Service)|
| Развёртывание| Render.com                          |
| Документация | drf-yasg (Swagger, Redoc)           |
| Статика      | WhiteNoise                          |

---

## 🧪 Тестирование и взаимодействие

- Swagger UI: [`/docs/`](https://django-rest-api-project.onrender.com/docs/)
- Пример запроса через `curl`:

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

## 📌 Пример использования

Подходит для создания платформы вакансий или внутреннего трекера проектов, где каждая вакансия привязана к конкретному 
проекту. API можно легко интегрировать с фронтендом или мобильным приложением.

