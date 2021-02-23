from django.urls import path
from .views import AboutCreateView
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('courses/',views.courses,name='courses'),
    path('courses/c/',views.c,name='c'),
    path('courses/python/',views.python,name='python'),
    path('courses/java/',views.java,name='java'),
    path('about/',AboutCreateView.as_view(),name='about'),
]
