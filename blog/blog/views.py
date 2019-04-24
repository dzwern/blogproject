from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse
from .models import Post


# Create your views here.
def index(request):
    # return HttpResponse("55")
    post_list=Post.objects.all().order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

def single(request,pk):
    post=get_list_or_404(Post,pk=pk)
    return render(request,'blog/single.html',context={'post':post})

