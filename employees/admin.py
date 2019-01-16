from django.contrib import admin
from . models import Employee as employee, News as news

# Register your models here.
admin.site.register(employee)
admin.site.register(news)
