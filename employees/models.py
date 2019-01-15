from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id = models.PositiveIntegerField()
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.firstName