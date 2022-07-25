from django.http import HttpResponse
from posts.models import Post


def index(request):
    if request.GET.get("key") == "test":
        return HttpResponse("Posts with test key")
    return HttpResponse("Posts index view")


def index(request):
    if request.GET.get('title'):
        post_list = Post.objects.filter(title__contains=request.GET.get('title'))
    else:
        post_list = Post.objects.all()
    return HttpResponse(" ".join(x.title for x in post_list))
