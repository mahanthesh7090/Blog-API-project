
from .models import Posts,Comment,User
from .serializers import PostsSerializer,CommentSerializer,UserSerializer,RegisterSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS,IsAuthenticatedOrReadOnly

#Persmissions for user only create delete and update
class IsOwnerOrReadOnly(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = GET, HEAD, OPTIONS
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user
    
#User Regidtartion
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny] 

#Post Creattion Endpoint API
class PostListCreate(ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

#Post Retrive Delete Update Endpoint API
class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class=PostsSerializer
    permission_classes = [IsOwnerOrReadOnly]

#Comments Creattion Endpoint API
class CommentDetails(RetrieveUpdateDestroyAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

#comments Retrive Delete Update Endpoint API
class CommentListCreate(ListCreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


