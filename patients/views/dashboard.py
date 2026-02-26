from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from patients.models import Patient

@login_required
def dashboard(request):
    total_patients = Patient.objects.count()
    return render(request, 'dashboard.html', {'total_patients': total_patients})