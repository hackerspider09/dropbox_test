# admin.py

from django.contrib import admin
from .models import Question, TestCase

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text',)
    search_fields = ('text',)

@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'input_data')
    search_fields = ('question__text',)
