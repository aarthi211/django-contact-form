from django.urls import path
from . import views

urlpatterns = [
    path('aarthi/', views.employee_form, name='aarthi'),
]