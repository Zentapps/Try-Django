from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from posts.models import Post
from websites.forms import UserForm,LoginForm
from django.contrib.auth import (
    authenticate,
)

def index(request):
    posts = Post.objects.filter(is_deleted=False)
    context = {
        'posts': posts
    }
    return render(request, 'websites/index.html', context)


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('websites:index'))
        else:
            form = UserForm(request.POST)
            context = {
                'form': form
            }
            return render(request, 'websites/register.html', context)
    else:
        form = UserForm()
        context = {
            'form': form
        }
        return render(request, 'websites/register.html', context)

from django.contrib.auth import login as auth_login, logout as auth_logout

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect(reverse('websites:index'))
            else:
                form = LoginForm()
                context = {
                    'form': form
                }
                return render(request, 'websites/login.html', context)

        else:
            form = LoginForm(request.POST)
            print(form.errors)
            context = {
                'form': form
            }
            return render(request, 'websites/login.html', context)
    else:
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'websites/login.html', context)



def post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'websites/post.html',{'post':post})

def logout(request):
    auth_logout(request)

    return HttpResponseRedirect(reverse('websites:index'))

def profile(request):
    return render(request,'websites/profile.html')
