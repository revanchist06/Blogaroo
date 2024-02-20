from django.shortcuts import render
from .models import BPost
# Create your views here.

def post_list(request):
    posts = BPost.objects.all()
    print("#"*100)
    print(posts)
    print(dir(posts))
    print("#"*100)
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})

def post_detail(request, id):
    post = BPost.objects.get(id=id)
    return render(request, 'blog/post/detail.html',{'post':post})


"""

def post_list(request):
    posts = Post.published.all()
    return render(request,
                 'blog/post/list.html',
                 {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post,
                             id=id,
                             status=Post.Status.PUBLISHED)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})

"""