from django.db import models
from django.utils import timezone


class Service(models.Model):
    SERVICE_CATEGORIES = [
        ('drywall', 'Drywall & Finishing'),
        ('framing', 'Metal & Wood Framing'),
        ('painting', 'Painting Services'),
        ('demolition', 'Demolition'),
        ('removal', 'Junk Removal'),
        ('insulation', 'Insulation'),
        ('doors', 'Door Installation'),
        ('ceiling', 'Acoustical Ceiling'),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=SERVICE_CATEGORIES)
    description = models.TextField()
    price_estimate = models.CharField(max_length=100, help_text="e.g., 'Starting at $500'")
    duration_estimate = models.CharField(max_length=100, help_text="e.g., '2-3 days'")
    icon = models.CharField(max_length=50, default='fa-tools', help_text="FontAwesome icon class")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_featured', 'name']

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    before_image = models.ImageField(upload_to='projects/before/', blank=True)
    after_image = models.ImageField(upload_to='projects/after/', blank=True)
    location = models.CharField(max_length=100)
    completion_date = models.DateField()
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-completion_date']

    def __str__(self):
        return self.title


class ContactInquiry(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('quoted', 'Quote Sent'),
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service_interested = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField()
    property_type = models.CharField(max_length=50, blank=True)
    timeline = models.CharField(max_length=100, blank=True)
    budget_range = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Contact Inquiries'

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d')}"


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    rating = models.IntegerField(default=5)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating} stars"
