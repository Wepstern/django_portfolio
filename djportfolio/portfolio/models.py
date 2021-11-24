from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.deletion import CASCADE

# Create your models here.

class Story(models.Model):
    text = models.TextField(max_length=5000, blank=False, default='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.') #TODO: remove default

class Expertise(models.Model):
    name = models.CharField(max_length=30, blank=False)
    description = models.TextField(max_length=5000, blank=False, default='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.') #TODO: remove default

class Skill(models.Model):
    name = models.CharField(max_length=30, blank=False, default='Black Magic')
    percentage = models.IntegerField(blank=False, default=60, 
    validators = [
        MaxValueValidator(100),
        MinValueValidator(0)
    ])
class Task(models.Model):
    description = models.TextField(max_length=1000, blank=False, default='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.') #TODO: remove default

class Job(models.Model):
    work_from = models.DateField(blank=False)
    work_till = models.DateField(blank=True)
    position = models.CharField(max_length=30, blank=False)
    company = models.CharField(max_length=30, blank=False)
    task = models.ManyToManyField(Task)
    current = models.BooleanField(blank=False, default=False)

    class Meta:
        ordering = ['-work_from']

class Study(models.Model):
    description = models.TextField(max_length=1000, blank=False, default='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.') #TODO: remove default

class Certificate(models.Model):
    study_from = models.DateField(blank=False)
    study_till =models.DateField(blank=True, null=True)
    certificate = models.CharField(max_length=100, blank=False)
    authority = models.CharField(max_length=100, blank=False)
    study = models.ManyToManyField(Study)
    current = models.BooleanField(blank=False, default=False)

    class Meta:
        ordering = ['-study_from']

class Topic(models.Model):
    name = models.TextField(max_length=50)

    class Meta:
        ordering = ['name']

class Project(models.Model):
    featured = models.BooleanField(blank=False, default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    preview_image = models.ImageField(blank=True, default='static/img/default.jpg') #TODO: remove default
    topic = models.ManyToManyField(Topic)

class User(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    birth_date = models.DateField(blank=False)
    profile_picture = models.ImageField(blank=True, default='static/img/default.jpg') #TODO: remove default
    profession = models.CharField(max_length=100, blank=False)
    story = models.ManyToManyField(Story)
    expertise = models.ManyToManyField(Expertise)
    skill = models.ManyToManyField(Skill)
    job = models.ManyToManyField(Job)
    certificate = models.ManyToManyField(Certificate)
    SEX_CHOICES = (
        ('Female', 'Female',),
        ('Male', 'Male',)
    )
    sex = models.CharField(
        max_length=6,
        choices=SEX_CHOICES,
    )
    project = models.ManyToManyField(Project)
    
    # there can be only one user
    def save(self, *args, **kwargs):
        if not self.pk and User.objects.exists():
            raise ValidationError('There is can be only one User instance.')
        return super(User, self).save(*args, **kwargs)
