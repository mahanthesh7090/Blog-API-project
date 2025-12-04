from django.shortcuts import render
from django.http import HttpResponse
from app.models import Post
from app.serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
# def home(request):
#     return HttpResponse("Hi")
@api_view(["GET","POST","DELETE"])
def post_list(request,id):
    if request.method=="GET":
        post=Post.objects.all()
        serlizer=PostSerializer(post,many=True)
        return Response(serlizer.data)
    if request.method=="POST":
        data=request.data
        serlizer=PostSerializer(data=data)
        if serlizer.is_valid():
            serlizer.save()
            return Response(serlizer.data,status=201)
        return Response(serlizer.errors,status=400)
    if request.method=="DELETE":
        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            return Response(status=404)
        
        post.delete()
        return Response(status=204)
    
