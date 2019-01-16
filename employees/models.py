from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'ID: {}, Name: {} {}, Date created: {}'.format(self.employee_id, self.first_name, self.last_name, self.date_created)

class News(models.Model):
    news_title = models.CharField(max_length=255)
    news_body = models.CharField(max_length=4095)
    # news_image = models.FileField(upload_to='images/', default='')
    date_created = models.DateTimeField(auto_now_add=True)
    employee_id = models.PositiveIntegerField(null=False)

    def __str__(self):
        return '{}; {}'.format(self.news_title, self.news_body)