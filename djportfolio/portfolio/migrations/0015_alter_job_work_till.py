# Generated by Django 3.2.8 on 2021-11-10 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_certificate_study'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='work_till',
            field=models.DateField(blank=True),
        ),
    ]