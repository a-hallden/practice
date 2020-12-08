import re

from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .client import Client
from .models import Favorites, Movie
from .serializers import FavoritesSerializer, MovieSerializer


# Create your views here.
class OMDBView(APIView):
    client = Client()

    def get_params(self, search_term):
        imdb_id_format = re.compile('^tt[0-9]{7,8}$')
        if imdb_id_format.match(search_term):
            param = 'i'
        else:
            param = 's'
        return {param: search_term}

    def get(self, request, *args, **kwargs):
        search_term = request.GET.get('search', None)
        if not search_term:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        params = self.get_params(search_term)
        response = self.client.search(params)
        if not response.get('Response') == 'True':
            return Response(
                response.get('Error'),
                status=status.HTTP_404_NOT_FOUND
            )
        if response.get('Search', False):
            return Response(response.get('Search'), status=status.HTTP_200_OK)
        return Response(response, status=status.HTTP_200_OK)


class FavoriteBaseView(APIView):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer


class FavoriteListView(FavoriteBaseView, generics.ListCreateAPIView):
    pass


class FavoriteDetailView(FavoriteBaseView, generics.RetrieveUpdateDestroyAPIView):
    pass
