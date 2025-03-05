from django.contrib import admin
from django.urls import path
from bank import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("create/", views.create_account, name="create_account"),
]
