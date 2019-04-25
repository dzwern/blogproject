from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.

from blog.models import Post

from .models import Comment

from .forms import CommentForm

def post_comment(request,post_pk):
    # 获取评论的文章
    #表达的含义是获取的文章不存在时，返回的是404界面
    post=get_object_or_404(Post,pk=post_pk)
    if request.method=="POST":
        # 构造实例
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect(post)

        else:
            comment_list=post.comment_set.all()
            context={
                'post':post,
                'form':form,
                'comment_list':comment_list
            }
            return render(request,'blog/detail.html',context=context)
    return redirect(post)



