from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile

def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = UserProfileForm()
    return render(request, 'create_profile.html', {'form': form})


def profile_list(request):
    profiles = UserProfile.objects.all()
    return render(request, 'profile_list.html', {'profiles': profiles})