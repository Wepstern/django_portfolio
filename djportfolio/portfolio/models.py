from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    birth_date = models.DateField(blank=False)
    profile_picture = models.ImageField(blank=True, default='static/img/default.jpg')
    profession = models.CharField(max_length=100, blank=False)
    SEX_CHOICES = (
        ('Female', 'Female',),
        ('Male', 'Male',)
    )
    sex = models.CharField(
        max_length=6,
        choices=SEX_CHOICES,
    )
    
    # there can be only one user
    def save(self, *args, **kwargs):
        if not self.pk and User.objects.exists():
            raise ValidationError('There is can be only one User instance.')
        return super(User, self).save(*args, **kwargs)
