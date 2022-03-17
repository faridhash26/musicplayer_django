from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Songs(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=False)
    artist = models.CharField(max_length=255, null=False)
    song = models.FileField(upload_to='songs/' , null=True)
    uploader = models.ForeignKey(User,null=True, blank=True, on_delete=models.SET_NULL)
    album = models.ImageField(upload_to ='album/',null=True)
    
    def __str__(self):
        return "{} - {} - {} - {}- {}-{}".format(self.id, self.title, self.artist, self.song , self.uploader ,self.album)
