# Generated by Django 3.2.3 on 2021-06-29 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210625_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='delivery_price',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
