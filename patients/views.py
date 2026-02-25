from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Patient


# -------------------
# LOGIN / LOGOUT
# -------------------

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


# -------------------
# DASHBOARD
# -------------------

@login_required
def dashboard(request):
    total_patients = Patient.objects.count()
    context = {'total_patients': total_patients}
    return render(request, 'dashboard.html', context)


# -------------------
# CRUD PATIENT
# -------------------

@login_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/list.html', {'patients': patients})


@login_required
def patient_create(request):
    if request.method == "POST":
        Patient.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            age=request.POST['age'],
            email=request.POST['email'],
            phone=request.POST['phone']
        )
        return redirect('patient_list')
    return render(request, 'patients/create.html')


@login_required
def patient_update(request, id):
    patient = get_object_or_404(Patient, id=id)
    if request.method == "POST":
        patient.first_name = request.POST['first_name']
        patient.last_name = request.POST['last_name']
        patient.age = request.POST['age']
        patient.email = request.POST['email']
        patient.phone = request.POST['phone']
        patient.save()
        return redirect('patient_list')
    return render(request, 'patients/update.html', {'patient': patient})


@login_required
def patient_delete(request, id):
    patient = get_object_or_404(Patient, id=id)
    patient.delete()
    return redirect('patient_list')