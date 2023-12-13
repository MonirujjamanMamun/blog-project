from django.shortcuts import render, redirect
from .forms import addPostForms
from .models import Posts

# Create your views here.


def add_post(request):
    if request.method == "POST":
        post_form = addPostForms(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('home')
    else:
        post_form = addPostForms()
    return render(request, 'add_post.html', {'form': post_form})


def edit_post(request, id):
    post = Posts.objects.get(pk=id)
    post_form = addPostForms(instance=post)
    if request.method == "POST":
        post_form = addPostForms(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('home')

    return render(request, 'add_post.html', {'form': post_form})


def delete_post(request, id):
    form = Posts.objects.get(pk=id)
    form.delete()
    return redirect('home')
