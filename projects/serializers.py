from django.utils import timezone
from datetime import timedelta
from rest_framework import serializers
from .models import Project, Vacancy

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__' #автоматически валидируются все поля модели

class ProjectSerializer(serializers.ModelSerializer):
    vacancies = VacancySerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__' #автоматически валидируются все поля модели

    def validate_deadline(self, value):
        """кастомная валидация поля дэдлайн"""
        tomorrow = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
        if value < tomorrow:
            raise serializers.ValidationError("Срок выполнения не может быть раньше завтрашнего дня.")
        return value
