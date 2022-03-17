from django.shortcuts import render
from rest_framework import generics ,filters
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

from .models import Songs
from .serializers import AllSongsSerializer, SongsSerializer

class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Songs.objects.all()
    serializer_class = AllSongsSerializer
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)

class PostSongsView(APIView):
    def post(self,request ,*args,**kwargs):
        serializer = SongsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CurrentSong(generics.RetrieveAPIView):
    lookup_field = 'id'
    lookup_url_kwarg="song_id"
    serializer_class=SongsSerializer
    queryset=Songs.objects.all()


