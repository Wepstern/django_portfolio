# Generated by Django 3.2.8 on 2021-11-30 20:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('study_from', models.DateField(blank=True, null=True)),
                ('study_till', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CertificateAuthority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('profile_picture', models.ImageField(upload_to='')),
                ('sex', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=6)),
                ('facebook', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
                ('github', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
                ('behance', models.URLField(blank=True, max_length=254)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='UserStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(max_length=50)),
                ('short_introduction', models.TextField(max_length=500)),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.user')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.FilePathField(path='/Users/baloghgergo/git/django_portfolio/djportfolio/media')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.user')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('featured', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(max_length=1000)),
                ('preview_image', models.ImageField(blank=True, upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portfolio.user')),
                ('category', models.ManyToManyField(to='portfolio.Category')),
                ('skill', models.ManyToManyField(to='portfolio.Skill')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.user')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
                ('work_from', models.DateField()),
                ('work_till', models.DateField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portfolio.company')),
                ('task', models.ManyToManyField(to='portfolio.Task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.user')),
            ],
            options={
                'ordering': ['-work_from'],
            },
        ),
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.user')),
            ],
        ),
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=1000)),
                ('percentage', models.IntegerField(default=60, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('certificate', models.ManyToManyField(blank=True, to='portfolio.Certificate')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portfolio.skill')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.user')),
            ],
        ),
        migrations.AddField(
            model_name='certificate',
            name='certificate_authority',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portfolio.certificateauthority'),
        ),
    ]
