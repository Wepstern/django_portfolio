# Generated by Django 3.2.8 on 2021-11-30 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_resume_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.ManyToManyField(blank=True, to='portfolio.Category'),
        ),
        migrations.AlterField(
            model_name='project',
            name='skill',
            field=models.ManyToManyField(blank=True, to='portfolio.Skill'),
        ),
    ]
