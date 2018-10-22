from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'blog/index.html')

def posts(request, post_id='1'):
    #Access post_id with 'post_id' variable
    return render(request, 'blog/blog.html')
