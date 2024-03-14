from django.db import models

# Create your models here.
# models.py

from django.db import models



class Question(models.Model):
    text = models.TextField()

class TestCase(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # input_data = models.FileField(upload_to='test_cases/input_data/')
    input_data = models.FileField(upload_to='test_cases/input_data/')

