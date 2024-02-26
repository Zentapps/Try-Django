from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from blogs.services import generate_form_errors
from django.contrib.auth.decorators import login_required
from posts.forms import PostForm
from posts.models import Post

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            data.save()
            return redirect(reverse('websites:post', args=[data.pk]))
        else:
            form = form
            errors  = generate_form_errors(form)
            context = {
                'title': 'Create Post',
                'form':form,
                'errors':errors,
            }
            return render(request, 'posts/entry_post.html',context)
    else:
        form = PostForm()
        context = {
            'title': 'Create Post',
            'form':form,

        }
        return render(request, 'posts/entry_post.html',context)

def list_post(request):
    instances = Post.objects.filter(is_deleted=False)
    context ={
        'instances':instances,
    }
    return render(request, 'posts/list_post.html',context)

@login_required
def edit_post(request,pk):
    post = get_object_or_404(Post,pk=pk,creator=request.user,is_deleted=False)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('posts:'))
        else:
            form = form
            errors  = generate_form_errors(form)
            context = {
                'title': 'Create Post',
                'form':form,
                'errors':errors,
            }
            return render(request, 'posts/entry_post.html',context)
    else:
        form = PostForm(instance=post)
        context = {
            'title': 'Create Post',
            'form':form,

        }
        return render(request, 'posts/entry_post.html',context)
