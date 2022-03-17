from rest_framework import serializers
from .models import Songs

class AllSongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ("id" , "title", "artist", "album")

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ("id" , "title", "artist", "song" , "uploader" , "album")