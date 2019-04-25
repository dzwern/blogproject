from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post,Category,Tag
from comment.forms import CommentForm
import markdown


# Create your views here.
def index(request):
    # return HttpResponse("55")
    post_list=Post.objects.all().order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})


def single(request,pk):
    post=get_object_or_404(Post,pk=pk)

    form=CommentForm()
    comment_list=post.comment_set.all()
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    post.body = md.convert(post.body)
    post.toc = md.toc

    context={'post':post,
             'form':form,
             'comment_list':comment_list

    }
    return render(request,'blog/single.html',context=context)


#归档
def archives(request,month):
    # __month表示的是删选月份
    post_list=Post.objects.all().filter(created_time__month=month)
    return render(request, 'blog/index.html', context={'post_list': post_list})


#分类
def classies(request,im):
    category=Category.objects.get(pk=im)
    post_list=category.post_set.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})


#标签
def tags(request,ip):
    tagies=Tag.objects.get(pk=ip)
    post_list=tagies.post_set.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})




