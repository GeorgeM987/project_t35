from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages
from django.utils import timezone
#
from app_users.decorators import unauthenticated_user, allowed_users
#
from .models import BlogPost
from .forms import BlogUpdateForm, BlogCreateForm

@login_required(login_url='app_users:login')
@allowed_users(allowed_roles=['admin', 'staff', 'users'])
def blog(request):
    posts = BlogPost.objects.all().order_by('date_posted')
    new_user = len(posts.filter(author=request.user)) == 0
    context = {'title': 'Blog', 'posts': posts, 'new_user': new_user}
    return render(request, 'app_blog/blog.html', context)

def blog_detail(request, pk):
    user_post = BlogPost.objects.get(id=pk)
    context = {'title': 'Blog', 'user_post': user_post}
    return render(request, 'app_blog/blog_detail.html', context)

def blog_user_detail(request, pk):
    user_detail = BlogPost.objects.get(id=pk)
    user_type = user_detail.author.groups.all()[0].name.capitalize()
    context = {'title': 'Blog', 'user_detail': user_detail, 'user_type': user_type}
    return render(request, 'app_blog/blog_user_detail.html', context)

def blog_create(request, pk):
    if request.method == 'POST':
        blog_creates = BlogCreateForm(request.POST)
        if blog_creates.is_valid():
            post = blog_creates.save(commit=False)
            post.author = request.user
            post.author.profile.image = request.FILES
            post.save()
            messages.success(request, 'Your blog-post has been created!')
            return redirect('app_blog:blog')
    else:
        blog_creates = BlogCreateForm()
    context = {'title': 'Blog', 'blog_creates': blog_creates}
    return render(request, 'app_blog/blog_create.html', context)

def blog_update(request, pk):
    if request.method == 'POST':
        blog_updates = BlogUpdateForm(request.POST, instance=BlogPost.objects.get(id=pk))
        if blog_updates.is_valid():
            blog_updates.save()
            messages.success(request, 'Your blog-post has been updated!')
            return redirect('app_blog:blog_detail', pk)
    else:
        blog_updates = BlogUpdateForm(instance=BlogPost.objects.get(id=pk))
    context = {'title': 'Blog', 'blog_updates': blog_updates}
    return render(request, 'app_blog/blog_update.html', context)

def blog_delete(request, pk):
    post_delete = BlogPost.objects.get(id=pk)
    if request.method == 'POST':
        post_delete.delete()
        return redirect('app_blog:blog')
    context = {'title': 'Blog', 'post_delete': post_delete}
    return render(request, 'app_blog/blog_delete.html', context)
