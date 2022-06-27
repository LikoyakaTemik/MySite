
from django.contrib import admin
from django.urls import path
from zeroone import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Menu)
]
