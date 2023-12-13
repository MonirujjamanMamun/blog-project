from django.shortcuts import render, redirect
from .forms import addAuthorForms

# Create your views here.


def add_author(request):
    if request.method == "POST":
        author_form = addAuthorForms(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('add_authors')
    else:
        author_form = addAuthorForms()
    return render(request, 'add_author.html', {'form': author_form})
