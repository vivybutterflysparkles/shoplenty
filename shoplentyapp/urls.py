
from django.contrib import admin
from django.urls import path
from shoplentyapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('gallery/', views.gallery,name="gallery"),
    path('info/', views.info,name="info"),
    path('form/', views.form,name="form"),
    path('login/', views.login,name="login"),
    path('register/', views.register,name="register"),
]
