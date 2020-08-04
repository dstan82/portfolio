from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.
def allblogs(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'blog/allblogs.html', {'posts':posts})

def detail(request, blog_id):
    detailpost = get_object_or_404(Post, pk=blog_id)
    return render(request, 'blog/detail.html', {'post':detailpost})
