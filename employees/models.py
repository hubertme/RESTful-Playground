from django.db import models
from django.utils.timezone import now

# Create your models here.
class Employee(models.Model):
    employee_id = models.PositiveIntegerField()
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    date_created = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.firstName