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
    list_display = ['title', 'service', 'location', 'completion_date', 'is_featured']
    list_filter = ['service', 'is_featured', 'completion_date']
    search_fields = ['title', 'description', 'location']
    date_hierarchy = 'completion_date'

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'service_interested', 'status', 'created_at']
    list_filter = ['status', 'service_interested', 'created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['status']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'service', 'is_active', 'created_at']
    list_filter = ['rating', 'is_active', 'service']
    search_fields = ['name', 'content']
    list_editable = ['is_active']
