from django.contrib import admin
from .models import User, Story, Expertise, Skill, Task, Job, Study, Certificate

# Register your models here.
admin.site.register(User)
admin.site.register(Story)
admin.site.register(Expertise)
admin.site.register(Skill)
admin.site.register(Task)
admin.site.register(Job)
admin.site.register(Study)
admin.site.register(Certificate)
