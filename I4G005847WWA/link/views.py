from rest_framework import ListAPIView
from rest_framework import CreateAPIView
from rest_framework import DetailAPIView
from rest_framework import UpdateAPIView
from rest_framework import DeleteAPIView
from .models import link
from .serializer import linkSerializer
# Create your views here.



class PostListApi(ListAPIView):
    queryset = link.object.filter(active = True)
    serializer_class = linkSerializer

class PostCreateApi(CreateAPIView):
    queryset = link.objects.filter(active = True)
    serializer_class = linkSerializer

class PostDetaileApi(DetailAPIView):
    queryset = link.objects.filter(active = True)
    serializer_class = linkSerializer 

class PostUpdateApi(UpdateAPIView):
    queryset = link.objects.filter(active = True)
    serializer_class = linkSerializer       

class PostDeleteApi(DeleteAPIView):
    queryset = link.objects.filter(active = True)
    serializer_class = linkSerializer       