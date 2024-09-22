from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()


def userlist(request):
    return render(request, 'privatechat/userlist.html', {})


def privatechat(request, username):
    user_obj = User.objects.get(username=username)
    return render(request, 'privatechat/privatechat.html', context={'user': user_obj})
