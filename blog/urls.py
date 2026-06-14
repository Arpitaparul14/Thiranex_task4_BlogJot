from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my-posts/', views.my_posts, name='my_posts'),
    path('notifications/', views.notifications, name='notifications'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('post/<slug:slug>/delete/', views.post_delete, name='post_delete'),
    path('post/<slug:slug>/like/', views.like_post, name='like_post'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]