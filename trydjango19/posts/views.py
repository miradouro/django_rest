from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.


def post_index(request):
    context = {
            "title": "Joao"
        }
    return render(request, "index.html", context)


def post_list(request):
    queryset = Post.objects.all()
    context = {
            "object_list": queryset,
            "title": "List"
        }
    return render(request, "index.html", context)
    #return HttpResponse("<h1>LIST</h1>")


def post_create(request):
    return HttpResponse("<h1>CREATE</h1>")


def post_detail(request):
    return HttpResponse("<h1>DETAIL</h1>")


def post_update(request):
    return HttpResponse("<h1>UPDATE</h1>")


def post_delete(request):
    return HttpResponse("<h1>DELETE</h1>")




