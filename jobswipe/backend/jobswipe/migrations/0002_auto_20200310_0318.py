# Generated by Django 3.0.4 on 2020-03-10 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobswipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saved',
            name='title',
            field=models.CharField(default='Saved Jobs', max_length=100),
        ),
        migrations.AlterField(
            model_name='unreviewed',
            name='title',
            field=models.CharField(default='Unreviewed Jobs', max_length=100),
        ),
    ]
