from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import User

def index(request):
    users = User.objects.all()

    if len(users) == 1:
        user = users[0]
    else:
        #TODO: Landing page -> Redirect to admin page
        raise ObjectDoesNotExist('There is no user in the database, please register one on the admin site!')

    context = {
        'user': user,
    }

    return render(request, 'index.html', context)
