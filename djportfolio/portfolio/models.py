from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.deletion import CASCADE, PROTECT

class User (models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    birth_date = models.DateField(blank=False)
    profile_picture = models.ImageField(blank=False)
    SEX_CHOICES = (
        ('Female', 'Female',),
        ('Male', 'Male',)
    )
    sex = models.CharField(max_length=6, choices=SEX_CHOICES, blank=False)
    facebook = models.URLField(max_length = 200, blank=True)
    linkedin = models.URLField(max_length = 200, blank=True)
    github = models.URLField(max_length = 200, blank=True)
    instagram = models.URLField(max_length = 200, blank=True)
    behance = models.URLField(max_length=254, blank=True)
    email = models.EmailField(max_length=254, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    path = models.FileField(upload_to='uploads/resume/')

    def __str__(self):
        return "Resume of " + self.user.__str__()

class CertificateAuthority(models.Model):
    name = models.CharField(max_length=100, blank=False)
    
    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=False)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    name = models.CharField(max_length=100, blank=False)
    study_from = models.DateField(blank=True, null=True)
    study_till =models.DateField(blank=True, null=True)
    certificate_authority = models.ForeignKey(CertificateAuthority, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name

class Profession(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    position = models.CharField(max_length=100, blank=False)
    work_from = models.DateField(blank=False)
    work_till =models.DateField(blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    task = models.ManyToManyField(Task)

    class Meta:
        ordering = ["-work_from"]

    def __str__(self):
        return self.position + " at " + self.company.name

class UserStory (models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE, blank=True)
    quote = models.CharField(max_length=50, blank=False)
    short_introduction = models.TextField(max_length=500, blank=False)

    def __str__(self):
        return self.quote

class Introduction (models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, blank=True)
    quote = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=500, blank=False)

    def __str__(self):
        return self.quote

class Expertise (models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, blank=True)
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT)
    description = models.TextField(max_length=1000, blank=False)
    percentage = models.IntegerField(blank=False, default=60, 
    validators = [
        MaxValueValidator(100),
        MinValueValidator(0)
    ])
    certificate = models.ManyToManyField(Certificate, blank=True)

    def __str__(self):
        return "Expertise in " + self.skill.name

class Project (models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=100, blank=False)
    featured = models.BooleanField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=1000, blank=False)
    preview_image = models.ImageField(blank=True)
    skill = models.ManyToManyField(Skill, blank=True)
    category = models.ManyToManyField(Category, blank=True)

    class Meta:
        ordering = ["-created"]

    def __str__ (self):
        return self.title + " by " + self.author.__str__()
