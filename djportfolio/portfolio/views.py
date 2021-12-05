from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Expertise, Introduction, User, Project, UserStory, Job, Resume
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings

from datetime import datetime
import os

def index(request):
    if request.method == 'POST' and 'Contact' in request.POST:
        dateTimeObj = datetime.now()

        contact_form = ContactForm(request.POST)

        contact_form.contact_email = request.POST['contact_email']
        contact_form.contact_message = request.POST['contact_message']

        if contact_form.is_valid():
            subject = 'Someone tried to contact you at ' + dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)") + ' !'
            message = 'Email from: ' + contact_form.contact_email + "\n" + contact_form.contact_message
            email_from = str(settings.EMAIL_HOST_USER)
            email_to = str(settings.DJANGO_ADMIN_EMAIL)

            send_mail(
                subject, 
                message,
                email_from,
                [email_to],
                html_message=None,
            )
            
            return HttpResponseRedirect('/#contact')
    
    users = User.objects.all()

    #currently only one user can be in the database TODO: Rewrite this sh*tty, temporary workaround.
    user = users[0]

    # if len(users) == 1:
    #     user = users[0]
    # else:
    #     raise ObjectDoesNotExist('There is no user in the database, please register one on the admin site!')
    
    projects = Project.objects.filter(author=user)
    user_story = UserStory.objects.filter(user=user)
    introductions = Introduction.objects.filter(user=user)
    jobs = Job.objects.filter(user=user)
    expertises = Expertise.objects.filter(user=user)

    resume = Resume.objects.filter(user=user)

    #currently only one user / resume can be in the database TODO: Rewrite this sh*tty, temporary workaround.
    try:
        resume = resume[0]
    except:
        pass
    
    context = {
        'user': user,
        'projects': projects,
        'user_story': user_story,
        'introductions': introductions,
        'jobs': jobs,
        'expertises': expertises,
        'resume': resume,
    }

    return render(request, 'index.html', context)
