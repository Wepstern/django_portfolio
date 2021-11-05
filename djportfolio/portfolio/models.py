from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


class User(models.Model):
    firstName = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    birth_data = models.DateField(blank=False)
    profile_picture = models.ImageField(blank=True, default='default.jpg')
    SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',)
    )
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
    )

    # there can be only one user
    def save(self, *args, **kwargs):
        if not self.pk and User.objects.exists():
            raise ValidationError(
                'There is can be only one User instance')
        return super(User, self).save(*args, **kwargs)
