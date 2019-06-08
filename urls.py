

from django.conf.urls import url, include

from Learn.TogatherWeLearn import admin
from . import  views
app_name="Together We Learn"
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name="index"),
    url(r'^list/$', views.listSkills,name="list"),
    url(r'^list/$', views.user,name="sign"),
    url(r'^list/$', views.comment,),
    url(r'^list/$', views.showProfile,name="profile")



]

