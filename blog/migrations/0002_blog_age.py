# Generated by Django 5.0.3 on 2024-03-28 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='age',
            field=models.CharField(default=0, max_length=2),
        ),
    ]
