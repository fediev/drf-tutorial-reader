# Generated by Django 4.0.5 on 2022-07-04 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='highlighted',
            field=models.TextField(blank=True),
        ),
    ]
