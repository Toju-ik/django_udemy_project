from django.urls import path
from . import views

urlpatterns = [
    # if a request reaches /january then execute the index function found in the views.py file
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="monthly_challenge"),
]