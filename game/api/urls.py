from unicodedata import name
from .views import UserCreate,UserDetail,SaveResult, Game, certificate

from django.contrib import admin
from django.urls import path,re_path

urlpatterns = [
    re_path('saveresult/(?P<pk>\d+)/$', SaveResult.as_view(), name="save-result"),
    path('userdetail/',  UserDetail.as_view(), name="user-detail"),
    path('game/', Game.as_view(), name='game'),
    path('certificate/', certificate, name='certificate')
]