from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets


from .models import Publicidad,Clicks,Viewability
from .serializers import PublicidadSerializer,ClickSerializer,ViewableSerializer


# Create your views here.


class FacebookList(generics.ListCreateAPIView):
    queryset = Publicidad.objects.all()[:20]
    serializer_class = PublicidadSerializer


class FacebookDetalle(generics.RetrieveDestroyAPIView):
    queryset = Publicidad.objects.all()
    serializer_class = PublicidadSerializer


class FacebookCliks(generics.ListCreateAPIView):
    queryset = Clicks.objects.all()[:20]
    serializer_class = ClickSerializer


class FacebookViewable(generics.ListCreateAPIView):
    queryset = Viewability.objects.all()[:20]
    serializer_class = ViewableSerializer


class FacebookList_clicks(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Clicks.objects.filter(idAd_id=self.kwargs["pk"])
        return queryset
    serializer_class = ClickSerializer


class FacebookList_viewable(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Viewability.objects.filter(idAd_id=self.kwargs["pk"])
        return queryset
    serializer_class = ViewableSerializer


# vista lista en HTML

def list_facebook(request):
    fb=Publicidad.objects.all()
    return render(request,'list_fb.html' ,context={'facebook':fb})

