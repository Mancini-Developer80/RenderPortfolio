from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import BlogPost, Tag


def blog_home(request):
    """Blog homepage with list of published posts"""
    posts_list = BlogPost.objects.filter(is_published=True).order_by('-published_at')
    featured_posts = posts_list.filter(is_featured=True)[:3]
    
    # Pagination
    paginator = Paginator(posts_list, 9)  # 9 posts per page (3x3 grid)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    context = {
        'posts': posts,
        'featured_posts': featured_posts,
        'page_title': 'Blog',
    }
    return render(request, 'blog/blog_home.html', context)


def blog_detail(request, slug):
    """Single blog post detail page"""
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    
    # Increment view count
    post.increment_views()
    
    # Get related posts (same tags)
    related_posts = BlogPost.objects.filter(
        is_published=True,
        tags__in=post.tags.all()
    ).exclude(id=post.id).distinct()[:3]
    
    context = {
        'post': post,
        'related_posts': related_posts,
        'page_title': post.title,
    }
    return render(request, 'blog/blog_detail.html', context)


def tag_posts(request, slug):
    """Filter posts by tag"""
    tag = get_object_or_404(Tag, slug=slug)
    posts_list = BlogPost.objects.filter(is_published=True, tags=tag).order_by('-published_at')
    
    # Pagination
    paginator = Paginator(posts_list, 9)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    context = {
        'posts': posts,
        'tag': tag,
        'page_title': f'Tag: {tag.name}',
    }
    return render(request, 'blog/blog_home.html', context)


def blog_search(request):
    """Search blog posts"""
    query = request.GET.get('q', '')
    posts_list = BlogPost.objects.none()
    
    if query:
        posts_list = BlogPost.objects.filter(
            Q(title__icontains=query) |
            Q(excerpt__icontains=query) |
            Q(content__icontains=query),
            is_published=True
        ).order_by('-published_at')
    
    # Pagination
    paginator = Paginator(posts_list, 9)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    context = {
        'posts': posts,
        'query': query,
        'page_title': f'Search: {query}' if query else 'Search',
    }
    return render(request, 'blog/blog_home.html', context)
