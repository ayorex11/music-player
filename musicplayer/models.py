from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Musician(models.Model):
	name = models.CharField(max_length=100)
	


class Audio(models.Model):
	title = models.CharField(max_length=100)
	artist = models.ForeignKey(
		Musician, on_delete=models.CASCADE, related_name='audio')
	release_date = models.DateField(null=True)
	src = models.CharField(max_length=256)
	num_stars = models.IntegerField(null=True)
	song_file = models.FileField()
	owner = models.ForeignKey(
		User, on_delete=models.CASCADE, null=True)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	playlist = models.ManyToManyField(Audio)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
  if created:
    profile = Profile.objects.create(user=instance)
    profile.save()
  else:
    instance.profile.save()


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
  instance.profile.save()

