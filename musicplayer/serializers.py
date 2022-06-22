from rest_framework import serializers
from .models import Audio, Musician, Profile
from django.contrib.auth import authenticate







class AudioSerializer(serializers.ModelSerializer):


  class Meta:
    model = Audio
    fields = ('id', 'title', 'artist', 'src',)


class MusicianSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Musician
    fields = ('name',)


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Profile
    fields = ('playlist', )
