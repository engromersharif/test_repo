from django.contrib import admin

# Register your models here.g

# Test123
from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
