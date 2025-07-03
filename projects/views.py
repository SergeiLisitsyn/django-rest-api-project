from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Project, Vacancy
from .serializers import ProjectSerializer, VacancySerializer

class ProjectsViewSet(viewsets.ModelViewSet):
    # использем модуль viewsets который объединяет в одни класс отдельные функции или классы для GET, POST, PUT, DELETE
    queryset = Project.objects.all() # запрос выводит все проекты
    serializer_class = ProjectSerializer


class VacancyViewSet(viewsets.ModelViewSet):
    # использем модуль viewsets который объединяет в одни класс отдельные функции или классы для GET, POST, PUT, DELETE
    queryset = Vacancy.objects.all() # запрос выводит все имеющиеся вакансии
    serializer_class = VacancySerializer

    def create(self, request, *args, **kwargs):
        """костомные метод, который отвечает за создание новой вакансии через POST-запрос."""
        project_id = self.kwargs.get('project_pk') #project_id из вложенного URL
        try:
            project = Project.objects.get(pk=project_id)# проверяем наличие такого проекта
        except Project.DoesNotExist:
            return Response({'error': 'Проект не найден'}, status=status.HTTP_404_NOT_FOUND) #сообщение если проекта нет
        serializer = self.get_serializer(data=request.data) # получаем сериалайзер
        serializer.is_valid(raise_exception=True)
        serializer.save(project=project) # Сериализуем входящие данные и сохраняем вакансию для данного проекта
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        """кастомная функция для создания списка вакансий для заданного проекта"""
        project_id = self.kwargs.get('project_pk')# принимаем из url project id
        queryset = Vacancy.objects.filter(project_id=project_id)# запрос для вывода вакансий для проекта с указанным id
        serializer = self.get_serializer(queryset, many=True) # сериализуем полученный список
        return Response(serializer.data)
