from django.contrib import admin
from .models import Project, Vacancy


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','experience', 'field', 'description','deadline',)
    search_fields = ('name',)
    list_filter = ('name', 'field')
    actions = ['mark_deleted']

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('project','description',)
    search_fields = ('project',)
    list_filter = ('project',)
    actions = ['mark_deleted']