from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contents/', views.contents, name='contents'),
    path('contact/', views.contact, name='contact'),
    path('contact_form/', views.contact_form, name='contact_form'),
    path('comp/', views.comp, name='comp'),
]
