from django.urls import path
from detection.views import *

urlpatterns = [
    path("", predict, name="predict"),
    path('about',about,name="about_page"),
    path('usecase',usecase,name="usecase_page")
]