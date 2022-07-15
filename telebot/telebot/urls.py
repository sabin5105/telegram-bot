from django.contrib import admin
from django.urls import path, include
from user import views

#TODO: Add urls for user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register/', views.RegisterFormView.as_view(), name='register'),
    path('login/', views.LoginView.as_view()),
]