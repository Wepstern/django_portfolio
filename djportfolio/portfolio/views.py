from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Expertise, Introduction, User, Project, UserStory, Job, Resume
from django.http import FileResponse, Http404

def index(request):
    users = User.objects.all()

    #currently only one user can be in the database TODO: Rewrite this sh*tty, temporary workaround.
    if len(users) == 1:
        user = users[0]
    else:
        #TODO: Landing page -> Redirect to admin page
        # raise ObjectDoesNotExist('There is no user in the database, please register one on the admin site!')
        pass

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
