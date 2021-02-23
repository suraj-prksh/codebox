from django.urls import path
from .views import PostListView,PostDeleteView,UserPostListView,PostUpdateView,PostCreateView,PostDetailView,CommentDeleteView
from . import views

urlpatterns = [
    path('',PostListView.as_view(),name='discuss'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/comment/', views.add_comment_to_post,name='add_comment_to_post'),
    #path('comment/<int:pk>/remove/',views.comment_remove, name='comment_remove'),
    path('comment/<int:pk>/remove/',CommentDeleteView.as_view(),name='comment_remove'),
]
