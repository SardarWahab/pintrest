# Generated by Django 5.1 on 2024-10-09 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='DOB',
            field=models.DateField(blank=True, null=True),
        ),
    ]
