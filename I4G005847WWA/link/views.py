from django.shortcuts import render
from rest_framework import generics
from rest_framework import serializers
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DestroyAPIView
from .serializers import LinkSerializer
from .models import link



class PostListApi(ListAPIView):
    queryset = link.objects.filter(active = True)
    serializer_class = LinkSerializer

class PostCreateApi(CreateAPIView):
    queryset = link.objects.filter(active = True)
    serializer_class = LinkSerializer

class PostDetaileApi(RetrieveAPIView):
    queryset = link.objects.filter(active = True)
    serializer_class = LinkSerializer 

class PostUpdateApi(UpdateAPIView):
    queryset = link.objects.filter(active = True)
    serializer_class = LinkSerializer       

class PostDeleteApi(DestroyAPIView):
    queryset = link.objects.filter(active = True)
    serializer_class = LinkSerializer      