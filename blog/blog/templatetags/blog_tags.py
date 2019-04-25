from ..models import Post,Category,Tag
from django import template

#实例化template.Library类
register= template.Library()


#最新文章模板标签
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


#归档模板标签
@register.simple_tag
def archives():
    return Post.objects.dates('created_time','month',order='DESC')


#分类模板标签
@register.simple_tag
def get_categories():
    return Category.objects.all()

#标签模板的
@register.simple_tag
def get_tags():
    return Tag.objects.all()


