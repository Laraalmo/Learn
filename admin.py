from django.contrib import admin

# Register your models here.
from .models import*
admin.site.register(User)
admin.site.register(Volunteer)
admin.site.register(Learner)
admin.site.register(Comment)