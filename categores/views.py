from django.shortcuts import render, redirect
from .forms import addCategoresForms

# Create your views here.


def add_categores(request):
    if request.method == "POST":
        categores_form = addCategoresForms(request.POST)
        if categores_form.is_valid():
            categores_form.save()
            return redirect('add_categores')
    else:
        categores_form = addCategoresForms()
    return render(request, 'add_categores.html', {'form': categores_form})
