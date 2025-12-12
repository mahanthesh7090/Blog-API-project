
from .models import Posts,Comment,User
from .serializers import PostsSerializer,CommentSerializer,UserSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

#Post Creattion Endpoint API
class PostListCreate(ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
#Post Retrive Delete Update Endpoint API
class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class=PostsSerializer
#Comments Creattion Endpoint API
class CommentDetails(RetrieveUpdateDestroyAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
#comments Retrive Delete Update Endpoint API
class CommentListCreate(ListCreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer


