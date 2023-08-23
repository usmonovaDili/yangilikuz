from django.shortcuts import render
from .models import News
from .serializers import NewsSerializers
from rest_framework import generics


class NewsSlug(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers


class NewsAll(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers


class NewsUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
