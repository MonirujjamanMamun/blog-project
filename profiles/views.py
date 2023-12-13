from django.shortcuts import render, redirect
from .forms import addProfileForm
# Create your views here.


def add_profiles(request):
    if request.method == "POST":
        profiles_form = addProfileForm(request.POST)
        if profiles_form.is_valid():
            profiles_form.save()
            return redirect('add_profiles')
    else:
        profiles_form = addProfileForm()
    return render(request, 'add_profile.html', {'form': profiles_form})
