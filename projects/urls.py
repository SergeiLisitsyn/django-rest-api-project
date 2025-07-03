from rest_framework_nested import routers
from .views import ProjectsViewSet, VacancyViewSet

"""создаёт два набора маршрутов API:
Обычные маршруты: /projects/ и /vacancies/ — для работы напрямую с проектами и вакансиями
Вложенные маршруты: /projects/<id>/vacancies/ — для работы с вакансиями, принадлежащими конкретному проекту"""

router = routers.DefaultRouter() #создаем базовый маршрутизатор
router.register(r'projects', ProjectsViewSet, basename='project') #добавляем маршрут /projects/, который обрабатывает
                                                                  # GET, POST, PUT, DELETE для модели Project
router.register(r'vacancies', VacancyViewSet, basename='vacancy')  #добавляем маршрут /vacancies/,
                                                                   # работающий напрямую с моделью Vacancy
#Создаётся вложенный маршрутизатор, который «подключается» к маршруту /projects/.
# lookup='project' — это имя аргумента URL: project_pk, используемое внутри VacancyViewSet
projects_router = routers.NestedDefaultRouter(router, r'projects', lookup='project')

#Добавляем маршрут /projects/<project_id>/vacancies/, который показывает/создаёт вакансии, связанные с конкретным проектом.
projects_router.register(r'vacancies', VacancyViewSet, basename='project-vacancies')
#Собираем все маршруты — и обычные, и вложенные — в список urlpatterns
urlpatterns = router.urls + projects_router.urls
