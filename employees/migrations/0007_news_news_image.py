# Generated by Django 2.1.5 on 2019-01-16 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_auto_20190116_0426'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_image',
            field=models.FileField(default='', upload_to='images/'),
        ),
    ]