from django.contrib import admin

# Register your models here.
from .models import Customer,Project,Survey,Question,QuestionAnswer

admin.site.register(Customer)
admin.site.register(Project)
admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(QuestionAnswer)