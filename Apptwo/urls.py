from django.urls import path
from . import views
from Apptwo import views
app_name='Apptwo'
urlpatterns=[
path('',views.index,name='index'),
path('register/',views.entry,name='form'),
path('login/',views.loginpage,name='f'),
]
