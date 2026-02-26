from django.urls import path
from patients.views import (
    dashboard, user_login, user_logout,
    patient_list, patient_create, patient_update, patient_delete
)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    path('patients/', patient_list, name='patient_list'),
    path('patients/add/', patient_create, name='patient_create'),
    path('patients/<int:id>/edit/', patient_update, name='patient_update'),
    path('patients/<int:id>/delete/', patient_delete, name='patient_delete'),
]