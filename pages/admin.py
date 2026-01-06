from django.contrib import admin
from django.utils.html import format_html
from .models import Technology, CaseStudy, ContactSubmission


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_featured', 'created_at']
    list_filter = ['is_featured', 'technologies']
    search_fields = ['title', 'short_description']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['technologies']
    list_editable = ['order', 'is_featured']


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    """Admin interface for contact form submissions"""
    list_display = ['subject', 'name', 'email', 'status_badge', 'submitted_at']
    list_filter = ['status', 'submitted_at']
    search_fields = ['subject', 'name', 'email', 'message']
    readonly_fields = ['subject', 'name', 'email', 'message', 'submitted_at']
    list_per_page = 25
    date_hierarchy = 'submitted_at'
    
    fieldsets = (
        ('Submission Details', {
            'fields': ('subject', 'name', 'email', 'submitted_at')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Management', {
            'fields': ('status', 'notes')
        }),
    )
    
    def status_badge(self, obj):
        colors = {
            'unread': '#dc3545',
            'read': '#ffc107',
            'responded': '#28a745'
        }
        color = colors.get(obj.status, '#6c757d')
        return format_html(
            '<span style="background: {}; color: white; padding: 3px 10px; border-radius: 3px; font-weight: bold;">{}</span>',
            color,
            obj.get_status_display()
        )
    status_badge.short_description = 'Status'
    
    def has_add_permission(self, request):
        # Don't allow manual creation of submissions
        return False
