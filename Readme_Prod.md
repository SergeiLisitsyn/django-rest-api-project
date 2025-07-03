Подготавливаем
1. GitHub-репозиторий с проектом: https://github.com/SergeiLisitsyn/django-rest-api-project

2. gunicorn как WSGI-сервер устанавливаем библиотеку с помощью команды pip install gunicorn.

3. Файл с зависимостями requirements.txt. Используем команду pip freeze > requirements.txt

4. Dockerfile

5. В качестве базы данных будет использован POSTGRES которая будет подключена как сервис render. Для этого:
 В settings.py: меняем DATABASES

import dj_database_url
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}
Это позволит Django автоматически взять строку подключения из переменной DATABASE_URL.
6. Создаем runtime.txt и Procfile.

7. 


