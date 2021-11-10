# Generated by Django 3.2.8 on 2021-11-10 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20211110_0121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='job',
            name='task',
        ),
        migrations.AddField(
            model_name='job',
            name='task',
            field=models.ManyToManyField(to='portfolio.Task'),
        ),
    ]
