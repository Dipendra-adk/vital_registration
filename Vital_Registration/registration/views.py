from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import BirthRegistrationForm, DeathRegistrationForm, MarriageRegistrationForm, MigrationRegistrationForm, DivorceRegistrationForm



def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def contact(request):
    return render(request,'contact.html')


def birth_registration(request):
    if request.method == 'POST':
        form = BirthRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = BirthRegistrationForm()
    return render(request, 'birth_registration.html', {'form': form})

def death_registration(request):
    if request.method == 'POST':
        form = DeathRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = DeathRegistrationForm()
    return render(request, 'death_registration.html', {'form': form})

def marriage_registration(request):
    if request.method == 'POST':
        form = MarriageRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MarriageRegistrationForm()
    return render(request, 'marriage_registration.html', {'form': form})

def migration_registration(request):
    if request.method == 'POST':
        form = MigrationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MigrationRegistrationForm()
    return render(request, 'migration_registration.html', {'form': form})

def divorce_registration(request):
    if request.method == 'POST':
        form = DivorceRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = DivorceRegistrationForm()
    return render(request, 'divorce_registration.html', {'form': form})

def success(request):
    return render(request, 'registration/success.html')
