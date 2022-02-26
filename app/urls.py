from django.urls import path
from app import views
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contents/', views.contents, name='contents'),
    path('contact/', views.contact, name='contact'),
    path('contact_form', views.FormView.as_view(), name="contact_form"),
    path('comp/', views.comp, name='comp'),
]
