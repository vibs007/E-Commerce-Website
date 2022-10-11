
import imp
from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost

# Create your views here.
def index(request):
    myPosts = BlogPost.objects.all()
    return render(request, 'blog/index.html', {'myPosts':myPosts})

def blogpost(request, id):
    post = BlogPost.objects.filter(blog_id = id)[0]
    # print(post)
    return render(request, 'blog/blogpost.html',{'post':post})