from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Expertise, Introduction, User, Project, UserStory, Job

def index(request):
    users = User.objects.all()

    if len(users) == 1:
        user = users[0]
    else:
        #TODO: Landing page -> Redirect to admin page
        raise ObjectDoesNotExist('There is no user in the database, please register one on the admin site!')

    projects = Project.objects.filter(author=user)
    user_story = UserStory.objects.filter(user=user)
    introductions = Introduction.objects.filter(user=user)
    jobs = Job.objects.filter(user=user)
    expertises = Expertise.objects.filter(user=user)

    context = {
        'user': user,
        'projects': projects,
        'user_story': user_story,
        'introductions': introductions,
        'jobs': jobs,
        'expertises': expertises,
    }

    return render(request, 'index.html', context)
