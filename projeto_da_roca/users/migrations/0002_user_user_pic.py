# Generated by Django 3.2.3 on 2021-06-23 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_pic',
            field=models.ImageField(default='static/userImages/img_default.png', upload_to='static/userImages/'),
        ),
    ]
