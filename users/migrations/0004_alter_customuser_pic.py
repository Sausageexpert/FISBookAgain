# Generated by Django 4.1.5 on 2023-09-13 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='pic',
            field=models.ImageField(default='media/Dragonfruit.jpg', upload_to='profiles'),
        ),
    ]
