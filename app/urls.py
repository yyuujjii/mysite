from django.urls import path
from app import views
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contact_form/', views.contact_form, name='contact_form'),

]
