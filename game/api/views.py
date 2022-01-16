from ..models import User
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.views.generic import CreateView, FormView, DetailView, View, UpdateView
from rest_framework import generics
from .serializers import UserSerializer
from ..forms import UserCreateForm

class UserDetail(generics.ListAPIView):
    queryset= User.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        user= self.list(request, *args, **kwargs)
        return Response({'user': user.data}, template_name='game/result.html')

# class UserCreate(generics.CreateAPIView):
#     serializer_class = UserSerializer
#     queryset= User.objects.all()

#     def post(self, request, *args, **kwargs):
#         user= self.create(request, *args, **kwargs)
#         return Response({'user': user.data}, template_name='game.html')

class UserCreate(CreateView):
    form_class = UserCreateForm
    template_name = 'index.html'
    success_url = '/api/game/'


class SaveResult(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset= User.objects.all()

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class Game(CreateView):
    form_class = UserCreateForm
    template_name = 'game/game.html'
    success_url = '/api/userdetail/'

def certificate(request):
    return render(request,'game/certificate.html')