from django.conf.urls import url
from django.urls import path
from . import views
app_name='u'
urlpatterns = [
    path('',views.prof),
    path('password/', views.change_password, name='cp'),
    path('resume/',views.resume,name='resume')
]
