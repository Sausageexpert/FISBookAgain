# Generated by Django 4.1.5 on 2023-09-07 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0006_forum_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='pic',
            field=models.ImageField(default='media/forums/Dragonfruit2.jpg', upload_to='forums'),
        ),
    ]
