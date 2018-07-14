from django.shortcuts import render

from .models import Post

# --- Import HttpResponse just to test the views are connecting ---
from django.http import HttpResponse

def index(request):
    all_posts = Post.objects.all()
    dynamic_html = "<h1>Daniel's blog</h1>"
    for post in all_posts:
        dynamic_html += '<p>{}: {}</p>'.format(post.text, post.pub_date)
    return HttpResponse(dynamic_html)

def detail(request, post_id):
    try:
        post_detail = Post.objects.get(pk=post_id)
        dynamic_html = "<h1>Daniel's blog</h1><p>DateTime: {}</p><p>{}</p>".format(post_detail.text, post_detail.pub_date)
    except:
        dynamic_html = "<p>No post by that id!</p>"
    return HttpResponse(dynamic_html)
