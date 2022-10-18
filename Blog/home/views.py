from django.shortcuts import render
from .models import Post


# Create your views here.
def home(request):
    all_posts = Post.objects.all()[::-1]
    print(all_posts)
    return render(request, 'index.html', {'all_posts': all_posts})


def post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post.html', {'post': post})


def more_posts(request):
    n = 1
    all_posts = Post.objects.all()[0:n+1]
    return render(request, 'index.html', {'all_posts': all_posts})
