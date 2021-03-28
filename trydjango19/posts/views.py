from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.


def post_index(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "Index"
    }
    return render(request, "index.html", context)


def post_detail(request, abc):
    instance = get_object_or_404(Post, id=abc)
    context = {
            "title": instance.title,
            "instance": instance
        }
    return render(request, "post_detail.html", context)


def post_list(request):
    """queryset = Post.objects.all()
    context = {
            "object_list": queryset,
            "title": "List"
        }
    return render(request, "index.html", context)"""
    return HttpResponse("<h1>LIST</h1>")


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)

        instance.save()
    """if request.method == "POST":
        print(request.POST.get("title"))
        title = request.POST.get("content")
        Post.objects.create(title=title)"""
    context = {
        "form": form
    }
    return render(request, "post_form.html", context)


def post_update(request):
    return HttpResponse("<h1>UPDATE</h1>")


def post_delete(request):
    return HttpResponse("<h1>DELETE</h1>")




