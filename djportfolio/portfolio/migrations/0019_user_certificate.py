# Generated by Django 3.2.8 on 2021-11-10 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_alter_certificate_study_till'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='certificate',
            field=models.ManyToManyField(to='portfolio.Certificate'),
        ),
    ]