from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL for myapp
    path('form/', views.form, name='form'),  # URL for form
]