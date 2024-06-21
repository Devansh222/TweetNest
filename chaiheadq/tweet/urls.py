
from django.urls import path
from django.contrib import admin

from .import views

urlpatterns = [
    # path('', views.index,name='index'),
    
    path('', views.tweet_list,name='tweet_list'),
    path('admin/', admin.site.urls),
    path('create/', views.tweet_create,name='tweet_create'),
    path('<int:tweet_id>/edit/', views.tweet_edit,name='tweet_edit'),
    path('<int:tweet_id>/delete/', views.tweet_delete,name='tweet_delete'),
    path('register/', views.register,name='register'),
] 