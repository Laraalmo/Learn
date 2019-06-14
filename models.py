from django.db import models

# Create your models here.
#sgin in page (Profile or user)
class User(models.Model):
 FristName= models.CharField(max_length=12,null=True)
 LastName=models.CharField(max_length=12,null=True)
 Age=models.IntegerField(max_length=2,null=True)
 Image=models.FileField(null=False,blank=True)
 E_mail=models.EmailField(null=False,blank=True)
 JoinDate=models.TimeField(null=True)

 from django.contrib.auth.models import User
 from django.utils.translation import ugettext as _
 from userena.models import User

 class MyProfile(User):
  user = models.OneToOneField(User,unique=True,verbose_name=('user'),related_name='my_profile')
  favourite_snack = models.CharField(('favourite snack'),max_length=5)

def __str__(self):
    return self.TalentDescription
#skill
class Learner(User):
 SkillDescription=models.TextField(null=True)


#Volunteer page (Skill)
class Volunteer(User):
 CV=models.FileField(null=True)
 DatePublished=models.DateTimeField
 Location=models.CharField(max_length=20,null=False,blank=True)

def __str__(self):
    return self.Name
class Skill(models.Model):
  Skill=models.CharField


#comment page(comment)
class Comment(models.Model):
 user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
 Comment=models.TextField(max_length=400)
 Date=models.DateTimeField(null=True)





