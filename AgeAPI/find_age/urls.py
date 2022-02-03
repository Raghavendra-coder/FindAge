from django.urls import path
from . import views


urlpatterns = [
    path('get_age', views.GetAge.as_view()),
]