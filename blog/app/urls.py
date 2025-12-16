
from django.urls import path
from app import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
path('register/', views.RegisterView.as_view(), name='register'),
 path('posts', views.PostListCreate.as_view(), name='post-list-create'),
 path('posts/<int:pk>', views.PostDetail.as_view(), name='post-Details'), 
 path('comments', views.CommentListCreate.as_view(), name='comment-list-create'),
 path('comments/<int:pk>', views.CommentDetails.as_view(), name='comment-detail'),
   
]
urlpatterns = format_suffix_patterns(urlpatterns)