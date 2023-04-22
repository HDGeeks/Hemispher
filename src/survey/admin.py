from django.contrib import admin

# Register your models here.
from .models import Customer,Project,Survey,Question,QuestionAnswer

admin.site.register(Customer, Project,Survey,Question,QuestionAnswer)