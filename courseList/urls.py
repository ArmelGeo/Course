# from django.conf.urls import url  
# from django.contrib import admin  
# from courseList import views  

   
# app_name = 'courseList'  
   
# urlpatterns = [  
#     url('admin/', admin.site.urls),  
#     #url(r'^$', views.index, name='index'),  
#     url(r'^$', views.courses_list, name='courses_list'),  
#     url(r'^new$', views.courses_create, name='courses_new'),  
#     url(r'^edit/(?P<pk>\d+)$', views.courses_update, name='courses_edit'),  
#     url(r'^delete/(?P<pk>\d+)$', views.courses_delete, name='courses_delete'),
# ]

from django.conf.urls import url  
from django.contrib import admin  
from . import views  
   
app_name = 'courseList'  
   
urlpatterns = [  
    url('admin/', admin.site.urls),  
    url('', views.courses_list, name='courses_list'),  
    url(r'^create/$', views.courses_create, name='create'),  
    url(r'^edit/(?P<pk>[0-9]+)$', views.courses_edit, name='edit'),  
    url(r'^delete/(?P<pk>[0-9]+)$', views.courses_delete, name='delete'),
]