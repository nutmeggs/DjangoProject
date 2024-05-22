import re
from django.contrib import admin
from django.urls import path
from django.urls import include, re_path
import app.views
from app.views import studenthome


urlpatterns = [

    path('admin/', admin.site.urls),

    re_path(r'^$', app.views.index, name = 'index'),

    re_path(r'^home$', app.views.index, name = 'home'),

    path('studenthome/', studenthome, name='student_home'),

    path('dashboard/', app.views.add_item, name='dashboard'),
]







#from django.urls import path, include

#from .views import studenthome

#urlspattern = [
    #path("", studenthome, name='studenthome'),

#]
