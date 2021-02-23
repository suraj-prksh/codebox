from django.urls import path
from . import views

app_name = "ide"

urlpatterns = [
    path('',views.ide,name='ide'),
    path('run/',views.runCode,name='run'),
]
