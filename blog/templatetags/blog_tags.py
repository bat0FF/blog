from django import template
from django.db.models import Count
from ..models import Post
from django.utils.safestring import mark_safe
import markdown

register = template.Library()


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.inclusion_tag('blog/post/latest_posts.html')
def show_my_latest_posts(user, count=5):
    my_latest_posts = Post.published.filter(author=user).order_by('-publish')[:count]

    return {'latest_posts': my_latest_posts}



@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
        total_comments=Count('comments')
    ).exclude(total_comments=0).order_by('-total_comments')[:count]
