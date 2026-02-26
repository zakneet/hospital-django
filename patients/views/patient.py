from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from patients.models import Patient
from django.contrib import messages
from patients.forms import PatientForm
from django.db.models import Q

@login_required
def patient_list(request):
    q = request.GET.get("q", "").strip()
    patients = Patient.objects.all()

    if q:
        patients = patients.filter(
            Q(first_name__icontains=q) |
            Q(last_name__icontains=q) |
            Q(email__icontains=q) |
            Q(phone__icontains=q)
        )

    patients = patients.order_by("-created_at")
    return render(request, "patients/list.html", {"patients": patients, "q": q})

@login_required
def patient_create(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Patient created successfully!")
            return redirect("patient_list")
    else:
        form = PatientForm()
    return render(request, "patients/create.html", {"form": form})

@login_required
def patient_update(request, id):
    patient = get_object_or_404(Patient, id=id)
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, "Patient updated successfully!")
            return redirect("patient_list")
    else:
        form = PatientForm(instance=patient)
    return render(request, "patients/update.html", {"form": form})

@login_required
def patient_delete(request, id):
    patient = get_object_or_404(Patient, id=id)
    if request.method == "POST":
        patient.delete()
        messages.success(request, "Patient deleted successfully!")
        return redirect("patient_list")
    return render(request, "patients/delete.html", {"patient": patient})