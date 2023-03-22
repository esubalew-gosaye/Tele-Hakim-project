from django.urls import path
from . import views

urlpatterns = [
    path('', views.AppointmentView.as_view(), name="appointment"),
    path('', views.payment.as_view(), name="payment"),
]
