from django.shortcuts import render
from .models import Blogpost
# Create your views here.
from django.http import HttpResponse

def index(request):
    myposts = Blogpost.objects.all()
    if myposts not in request.session:
        request.session["myposts"]=[]
    else:
        return render(request, 'blog/index.html',
                  {'myposts': request.session["myposts"]})

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'blog/blogpost.html',
                  {'post':post})
