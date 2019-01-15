from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'ID: {}, Name: {} {}, Date created: {}'.format(self.employee_id, self.firstName, self.lastName, self.date_created)