from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Post
from .forms import PostForm

posts = [
    {
        'title': 'Beautiful is better than ugly',
        'author': 'John Doe',
        'content': 'Beautiful is better than ugly',
        'published_at': 'October 1, 2022'
    },
    {
        'title': 'Explicit is better than implicit',
        'author': 'Jane Doe',
        'content': 'Explicit is better than implicit',
        'published_at': 'October 1, 2022'
    }
]

def create_post(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request, 'blog/post_form.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been created successfully.')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blog/post_form.html', {'form': form})

def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'GET':
        context = {'form': PostForm(instance=post), 'id': id}
        return render(request,'blog/post_form.html',context)
    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been updated successfully.')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'blog/post_form.html',{'form':form})

def delete_post(request, id):
    post = get_object_or_404(Post, pk=id)
    context = {'post': post}    
    
    if request.method == 'GET':
        return render(request, 'blog/post_confirm_delete.html',context)
    elif request.method == 'POST':
        post.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('posts')

def home(request):
    posts = Post.objects.all()
    context = {'posts' : posts}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

