from django.urls import path, include
from .views import ListSongsView, PostSongsView,CurrentSong
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('songs/', ListSongsView.as_view(), name="songs-all"),
    path('songs/new/', csrf_exempt(PostSongsView.as_view()), name="songs-all"),
    path('songs/<int:song_id>/' ,CurrentSong.as_view() , name='current_song' )
]
