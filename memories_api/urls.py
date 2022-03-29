from django.urls import path, include  # added this whole file
from . import views

from knox import views as knox_views


urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', views.RegisterAPI.as_view()),
    path('api/auth/login', views.LoginAPI.as_view()),
    path('api/auth/user', views.UserAPI.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('api/users/', views.UserList.as_view(), name='user_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/users/<int:pk>', views.UserDetail.as_view(), name='user_detail'), # api/contacts will be routed to the ContactDetail view for handling
    path('api/auth/myposts/', views.MyMemoryList.as_view()),
    path('api/posts/', views.MemoryList.as_view()),
    path('api/posts/<int:pk>/', views.MemoryDetail.as_view()),
    path('api/post-favorites/', views.PostFavoriteList.as_view()),
    path('api/post-favorites/<int:pk>/', views.PostFavoriteDetail.as_view()),
    path('api/post-comments/', views.PostCommentList.as_view()),
    path('api/post-comments/<int:pk>/', views.PostCommentDetail.as_view())
   

]
