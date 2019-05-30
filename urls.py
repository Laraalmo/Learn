

from django.conf.urls import url, include
from . import  views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name="index")

]
