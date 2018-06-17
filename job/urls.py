from django.urls import path
from django.conf.urls import url
from . import views
app_name='job'
urlpatterns=[
path('',views.check,name='check'),
path('s/',views.joblist.as_view(),name='joblist'),
#path('s/<int:pk>', views.jobdetail.as_view(), name='jobdetail'),
url(r'^s/(?P<pk>\d+)/$',views.jobdetail.as_view(),name='jobdetail'),
path('trend',views.trending,name='trending')
]
