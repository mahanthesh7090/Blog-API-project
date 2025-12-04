
from django.urls import path
from app import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
  
  
    path("posts",views.post_list),
     path("posts/<int:id>",views.post_list),
]
urlpatterns = format_suffix_patterns(urlpatterns)