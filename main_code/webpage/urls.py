# from unicodedata import name
from django.urls import path
from . import views
from .views import (aboutPage, detailEmployees, employeesPage, homePage, mainPage,register_time_employee)
from django.urls import path
from .views import CustomLoginView



app_name = "webpage"

urlpatterns = [
     path('login/', CustomLoginView.as_view(), name='login'),
    path('', mainPage, name='webpage-view'),
    path('entenda-melhor/', homePage, name='homepage-view'),
    path('sobre/', aboutPage, name='aboutpage-view'),
    path('colaborador/',employeesPage,name='employeespage-view'),
    path('colaborador-info/<int:id>', detailEmployees, name='employeeinfo-view'),
    path('registrando-horario/',register_time_employee,name='register_time_employee'),
    path('',views.aboutPage),
]
