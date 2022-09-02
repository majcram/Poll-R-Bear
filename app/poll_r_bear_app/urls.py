from django.urls import path
from helloapp import views

urlpatterns = [
    path('', views.poll_r_bear, name='poll_r_bear'),
]