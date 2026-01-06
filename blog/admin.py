from django.contrib import admin
from django.utils.html import format_html
from .models import BlogPost, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Admin interface for blog tags"""
    list_display = ['name', 'slug', 'post_count']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    
    def post_count(self, obj):
        count = obj.posts.count()
        return format_html('<span style="font-weight: bold;">{}</span>', count)
    post_count.short_description = 'Posts'


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """Customized admin interface for blog posts"""
    list_display = ['title', 'author', 'status_badge', 'featured_badge', 'published_at', 'views_count', 'tags_list']
    list_filter = ['is_published', 'is_featured', 'created_at', 'tags']
    search_fields = ['title', 'excerpt', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    ordering = ['-published_at', '-created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'author', 'excerpt')
        }),
        ('Content', {
            'fields': ('content', 'featured_image')
        }),
        ('Organization', {
            'fields': ('tags',)
        }),
        ('Status & Features', {
            'fields': ('is_published', 'is_featured')
        }),
        ('SEO & Metadata', {
            'fields': ('meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('published_at', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
        ('Statistics', {
            'fields': ('views_count',),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at', 'views_count']
    filter_horizontal = ['tags']
    
    def save_model(self, request, obj, form, change):
        """Auto-assign current user as author if not set"""
        if not obj.author:
            obj.author = request.user
        super().save_model(request, obj, form, change)
    
    def status_badge(self, obj):
        if obj.is_published:
            return format_html('<span style="background: #28a745; color: white; padding: 3px 10px; border-radius: 3px;">Published</span>')
        return format_html('<span style="background: #6c757d; color: white; padding: 3px 10px; border-radius: 3px;">Draft</span>')
    status_badge.short_description = 'Status'
    
    def featured_badge(self, obj):
        if obj.is_featured:
            return format_html('<span style="color: #ffc107;">⭐</span>')
        return '-'
    featured_badge.short_description = 'Featured'
    
    def tags_list(self, obj):
        tags = obj.tags.all()
        if tags:
            tag_names = ', '.join([tag.name for tag in tags])
            return format_html('<span style="color: #397de2;">{}</span>', tag_names)
        return '-'
    tags_list.short_description = 'Tags'
