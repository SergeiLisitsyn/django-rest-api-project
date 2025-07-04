🚀 SmartCareer & CloudTask API
Live URL: https://django-rest-api-project.onrender.com 

📦 Overview
This is a Django REST API project. 

Built with Django REST Framework and deployed on Render, the API supports CRUD operations, nested relationships, and interactive documentation.

🧠 Features
🔗 RESTful endpoints for Projects and Vacancies
"projects": "https://django-rest-api-project.onrender.com/projects/",  returns the complete list of projects available in the system.

"vacancies": "https://django-rest-api-project.onrender.com/vacancies/" returns no data because each vacancy is linked to a specific project.

Vacancy retrieval is performed through the project’s ID. Use the endpoint projects/{id}/vacancies/ to return all vacancies associated with the given project.

🐘 PostgreSQL database integration. 
Connected to an internal PostgreSQL service provided by Render.com. ✅

🚀 Deployed on Render with CI/CD

📁 Project Structure
src/
├── projects/           # Project & Vacancy models, views, serializers
├── project_core/       # Main settings and URL routing
├── templates/          # Swagger/Redoc templates
├── staticfiles/        # Collected static assets
├── manage.py
🔌 API Endpoints
Projects
GET /projects/ – List all projects

POST /projects/ – Create a new project

GET /projects/{id}/ – Retrieve a project

PUT /projects/{id}/ – Update a project

DELETE /projects/{id}/ – Delete a project

Vacancies
GET /projects/{id}/vacancies/ – List all vacancies for project with id = {id}

POST /projects/{id}/vacancies/ – Create a vacancy for project with id = {id}

GET /vacancies/{id}/ – Retrieve a vacancy

PUT /vacancies/{id}/ – Update a vacancy

DELETE /vacancies/{id}/ – Delete a vacancy
Since the DRF HTML browser sends the "Delete" action via a plain form submission, without JavaScript it doesn't issue a proper DELETE request.

To delete a vacancy or project, you can use Postman or curl.

Example using curl in Git Bash:

bash
$ curl -X DELETE https://django-rest-api-project.onrender.com/projects/1/vacancies/2/


Nested
GET /projects/{project_id}/vacancies/ – List vacancies for a project

GET /projects/{project_id}/vacancies/{id}/ – Retrieve specific vacancy under a project

⚙️ Tech Stack
Layer	Technology
Backend	Django, Django REST Framework
Database	PostgreSQL
Deployment	Render
Docs	drf-yasg (Swagger, Redoc)
🚀 Deployment Notes
Hosted on Render using GitHub integration

PostgreSQL database provisioned via Render dashboard

Static files served via WhiteNoise

Build script includes:

bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
🧪 Local Setup
bash
git clone https://github.com/SergeiLisitsyn/django-rest-api-project.git
cd django-rest-api-project
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
👤 Admin Access
To create a superuser:

bash
python manage.py createsuperuser
Then visit: https://django-rest-api-project.onrender.com/admin/

📄 License
This project is licensed under the MIT License.


