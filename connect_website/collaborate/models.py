# C:\Users\Admin\connect_website\collaborate\models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#class Idea(models.Model):
   # user = models.ForeignKey(User, on_delete=models.CASCADE)
   # title = models.CharField(max_length=200)
    #description = models.TextField()
    #created_at = models.DateTimeField(auto_now_add=True)

   # def __str__(self):
       # return self.title
    
class Idea(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    occupation = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    sdg_goal = models.CharField(max_length=50)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ' - ' + self.description[:30]
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=50,
        choices=[('student', 'Student'), ('mentor', 'Mentor'), ('organization', 'Organization')]
    )
    interests = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
