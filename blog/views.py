from django.shortcuts import  get_object_or_404, render

from .models import Post

def index(request):
    all_posts = Post.objects.all()
    context = {'all_posts': all_posts}
    return render(request, 'blog/index.html', context)

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    context = {'a_post': post_detail}
    return render(request, 'blog/detail.html', context)
