from django.urls import path
from newhello import views

urlpatterns = [

    path('world/', views.hellofunction, name='hello'), 

]