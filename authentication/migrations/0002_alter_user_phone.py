# Generated by Django 3.2.7 on 2022-03-12 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(blank=True, db_index=True, null=True, unique=True),
        ),
    ]
