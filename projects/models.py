from django.db import models



class Project(models.Model):
    name = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()

    def __str__(self):
        """при выводе проекта будет вводиться название проекта"""
        return self.name

class Vacancy(models.Model):
    #Вакансия привязана к проекту
    project = models.ForeignKey('projects.Project', related_name='vacancies', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        """при выводе вакансии будет выводиться название проекта и описание вакансии"""
        return f"{self.project} @ {self.project.name}, {self.description}"