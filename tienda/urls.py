from django.contrib import admin
from django.urls import path
from tienda.views import display
from tienda.views import displayDateTime

urlpatterns = [
  path("admin/", admin.site.urls),
  path("hola/", display),
  path("ahora/", displayDateTime)
]