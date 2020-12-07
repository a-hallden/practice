from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from .client import Client


# Create your views here.
class SearchView(generics.ListAPIView):
    client = Client()

    def get(self, request, *args, **kwargs):
        search_term = request.GET.get('search', None)
        if not search_term:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        response = self.client.search(search_term)
        return Response(response.json(), status=status.HTTP_200_OK)
