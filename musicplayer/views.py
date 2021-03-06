from django.shortcuts import render
from django.http import HttpResponse

from .models import Audio, Musician, Profile
from .serializers import AudioSerializer,MusicianSerializer, ProfileSerializer

from rest_framework import viewsets, permissions



class AudioViewSet(viewsets.ModelViewSet):
  permission_classes = (
    permissions.AllowAny,
  )
  serializer_class = AudioSerializer
  queryset = Audio.objects.all()


class MusicianViewSet(viewsets.ModelViewSet):
  queryset = Musician.objects.all()
  permission_classes = [
    permissions.AllowAny,
  ]
  serializer_class = MusicianSerializer


class ProfileViewSet(viewsets.ModelViewSet):
  queryset = Profile.objects.all()
  permission_classes = [
    permissions.IsAuthenticated,
  ]
  serializer_class = ProfileSerializer

  def get_queryset(self):
    return (self.request.user.profile, )

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)
