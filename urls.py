

from django.conf.urls import url, include

from Learn.TogatherWeLearn import admin
from . import  views
app_name="Together We Learn"
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name="index"),
    url(r'^$', views.listSkills,name="list"),
    url(r'^$', views.user,name="sign"),
    url(r'^$', views.comment,),
    url(r'^$', views.showProfile,name="profile"),
    url(r'^accounts/', include('userena.urls')),



]

