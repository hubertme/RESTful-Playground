# Generated by Django 2.1.5 on 2019-01-16 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0008_remove_news_news_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_image',
            field=models.FileField(default='', upload_to='images/'),
        ),
    ]