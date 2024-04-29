from django.urls import path
from . import views

urlpatterns = [
    path('', views.recent_posts)
]
