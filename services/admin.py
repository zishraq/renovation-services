from django.contrib import admin
from .models import Service, Project, ContactInquiry, Testimonial


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price_estimate', 'is_featured', 'created_at']
    list_filter = ['category', 'is_featured']
    search_fields = ['name', 'description']
    list_editable = ['is_featured']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'badge_text', 'badge_color', 'is_featured', 'is_hero', 'order', 'service', 'location', 'completion_date', 'is_featured']
    list_filter = ['service', 'badge_color', 'is_featured', 'is_hero', 'badge_color', 'completion_date']
    search_fields = ['title', 'description', 'location']
    list_editable = ['is_featured', 'is_hero', 'order']
    date_hierarchy = 'completion_date'

    fieldsets = (
        (
            'Basic Information', {
                'fields': ('title', 'description', 'service', 'location', 'completion_date')
            }
        ),
        (
            'Images', {
                'fields': ('image', 'before_image', 'after_image')
            }
        ),
        (
            'Display Settings', {
                'fields': ('badge_text', 'badge_color', 'is_featured', 'is_hero', 'order'),
                'description': 'Note: Only ONE project should have "is_hero" checked. It will automatically uncheck others.'
            }
        )
    )


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'service_interested', 'status', 'created_at']
    list_filter = ['status', 'service_interested', 'created_at']
    search_fields = ['name', 'email', 'phone', 'message']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'
    list_editable = ['status']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'rating', 'service', 'is_active', 'created_at']
    list_filter = ['rating', 'is_active', 'service', 'created_at']
    search_fields = ['name', 'content']
    list_editable = ['is_active']
