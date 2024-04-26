from django.urls import path
from security import views

urlpatterns = [
    path('', views.home, name="home")
]
