from django.urls import path

from . import views # import view dari blog untuk home, 
from .views import PostListView, PostDetailView, PostCreateView # import views dari blog untuk ListView (bisa digunakan bisa tidak)

urlpatterns = [
        path('', views.PostListView.as_view(), name='blog-home'),
        path('user/<str:username>/', views.UserPostListView.as_view(), name='user-post'),
        path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
        path('post/new/', views.PostCreateView.as_view(), name='post-create'), # url create
        path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'), # url update
        path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
        path('about/', views.about, name='blog-about'),
        
    ]
