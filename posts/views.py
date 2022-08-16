from django.http import HttpResponse
from django.shortcuts import render

from posts.models import Post
from posts.forms import AddPosts
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# def index(request):
#     if request.GET.get("key") == "test":
#         return HttpResponse("Posts with test key")
#     return HttpResponse("Posts index view")
#
#
# def index(request):
#     if request.GET.get('title'):
#         post_list = Post.objects.filter(title__contains=request.GET.get('title'))
#     else:
#         post_list = Post.objects.all()
#     return HttpResponse(" ".join(x.title for x in post_list))

def index(request):

    post_list = Post.objects.all()
    return render(request, "index.html", {"index": post_list})


def add_posts(request):
    notes = Post.objects.all()
    if request.method == "POST":
        form = AddPosts(request.POST)
        if form.is_valid():
            Post.objects.create(
                title=form.cleaned_data["title"], text=form.cleaned_data["text"]
            )
            return redirect("index")
    else:
        form = AddPosts()
    return render(request, {"add_posts.html": notes, "form": form})
