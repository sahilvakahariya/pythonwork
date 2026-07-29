import csv
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Profile
from .forms import ProfileForm


# ---------- LIST VIEW ----------
def profile_list(request):
    profiles = Profile.objects.all().order_by('-created_at')
    return render(request, 'profiles/profile_list.html', {'profiles': profiles})


# ---------- CREATE VIEW ----------
def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm()
    return render(request, 'profiles/profile_form.html', {'form': form, 'action': 'Create'})


# ---------- EDIT VIEW ----------
def profile_edit(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profiles/profile_form.html', {'form': form, 'action': 'Edit'})


# ---------- EXPORT TO CSV VIEW ----------
def profile_export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="profiles_export.csv"'

    profiles = Profile.objects.all()

    # Using csv.writer directly on the HttpResponse (acts like a file object)
    writer = csv.writer(response)
    writer.writerow(['Username', 'Email', 'Age', 'Bio', 'Is Public', 'Created At'])

    for profile in profiles:
        writer.writerow([
            profile.username,
            profile.email,
            profile.age,
            profile.bio,
            profile.is_public,
            profile.created_at,
        ])

    return response


# ---------- Optional: Export to a local file using a context manager ----------
def profile_export_to_disk():
    """
    Demonstrates explicit use of a context manager (with open(...) as file:)
    to write DB records to a CSV file on disk, as required by the assessment.
    """
    profiles = Profile.objects.all()
    with open('profiles_backup.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Username', 'Email', 'Age', 'Bio', 'Is Public', 'Created At'])
        for profile in profiles:
            writer.writerow([
                profile.username, profile.email, profile.age,
                profile.bio, profile.is_public, profile.created_at
            ])
    print("Export complete: profiles_backup.csv")