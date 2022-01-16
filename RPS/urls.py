
from django.contrib import admin
from django.urls import path,include
from game.api.views import UserCreate
from .views import help_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UserCreate.as_view(), name='user-create'),
    path('help/', help_page, name='help'),
    path('api/', include('game.api.urls'))
]
