from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('getFace', views.getFace, name='getFace'),
    path('filledform',views.filledform, name='filledform'),
    path('loadFace',views.loadFace, name='loadFace'),
    path('registerComplete',views.registerComplete,name='registerComplete'),
    path('registerUser',views.registerUser, name='registerUser')
]