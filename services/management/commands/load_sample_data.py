from django.core.management.base import BaseCommand
from services.models import Service, Project, Testimonial
from django.utils import timezone
from datetime import timedelta
import random
import os
from django.conf import settings


class Command(BaseCommand):
    help = 'Load sample data for the renovation services website'

    def handle(self, *args, **kwargs):
        self.stdout.write('Loading sample data...')

        # Clear existing data
        Service.objects.all().delete()
        Project.objects.all().delete()
        Testimonial.objects.all().delete()

        # Create Services
        services_data = [
            {
                'name': 'Drywall Installation & Finishing',
                'category': 'drywall',
                'description': 'Professional drywall installation, taping, mudding, and finishing. We ensure perfectly smooth walls ready for painting. Our experts handle both residential and commercial projects with attention to detail.',
                'price_estimate': 'Starting at $500',
                'duration_estimate': '2-5 days',
                'icon': 'fa-paint-roller',
                'is_featured': True
            },
            {
                'name': 'Metal & Wood Framing',
                'category': 'framing',
                'description': 'Expert framing services for walls, ceilings, and structural modifications. We work with both metal studs and traditional wood framing to create solid foundations for your renovation.',
                'price_estimate': 'Starting at $800',
                'duration_estimate': '3-7 days',
                'icon': 'fa-hammer',
                'is_featured': True
            },
            {
                'name': 'Interior & Exterior Painting',
                'category': 'painting',
                'description': 'Transform your space with our professional painting services. We use premium paints and proven techniques to deliver flawless finishes that last for years.',
                'price_estimate': 'Starting at $400',
                'duration_estimate': '1-3 days',
                'icon': 'fa-paint-brush',
                'is_featured': True
            },
            {
                'name': 'Demolition Services',
                'category': 'demolition',
                'description': 'Safe and efficient demolition for renovation projects. We handle everything from small interior walls to complete gut renovations, ensuring proper disposal and site cleanup.',
                'price_estimate': 'Starting at $600',
                'duration_estimate': '1-2 days',
                'icon': 'fa-house-damage'
            },
            {
                'name': 'Junk Removal & Cleanup',
                'category': 'removal',
                'description': 'Complete cleanup and disposal of construction debris, old materials, and unwanted items. We ensure your site is clean and ready for the next phase.',
                'price_estimate': 'Starting at $300',
                'duration_estimate': 'Same day',
                'icon': 'fa-trash-alt'
            },
            {
                'name': 'Insulation Installation',
                'category': 'insulation',
                'description': 'Energy-efficient insulation for walls, attics, and crawl spaces. Reduce energy costs and improve comfort with our professional insulation services.',
                'price_estimate': 'Starting at $1,200',
                'duration_estimate': '2-3 days',
                'icon': 'fa-temperature-low'
            },
            {
                'name': 'Door Installation',
                'category': 'doors',
                'description': 'Professional installation of interior and exterior doors. From standard doors to custom installations, we ensure perfect fit and smooth operation.',
                'price_estimate': 'Starting at $350',
                'duration_estimate': '4-6 hours',
                'icon': 'fa-door-open'
            },
            {
                'name': 'Acoustical Ceiling',
                'category': 'ceiling',
                'description': 'Drop ceiling and acoustical tile installation for commercial and residential spaces. Improve sound quality and aesthetics with our ceiling solutions.',
                'price_estimate': 'Starting at $700',
                'duration_estimate': '2-4 days',
                'icon': 'fa-th'
            }
        ]

        services = []
        for data in services_data:
            service = Service.objects.create(**data)
            services.append(service)
            self.stdout.write(f'Created service: {service.name}')

        # Get list of available images
        gallery_path = os.path.join(settings.MEDIA_ROOT, 'projects', 'gallery')
        available_images = []

        if os.path.exists(gallery_path):
            available_images = [f for f in os.listdir(gallery_path)
                                if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
            self.stdout.write(f'Found {len(available_images)} images in gallery')
        else:
            self.stdout.write(self.style.WARNING(f'Gallery path not found: {gallery_path}'))

        # Create Projects with images and badge colors
        projects_data = [
            {
                'title': 'Warehouse Framing Project',
                'description': 'Commercial office space with modern grid system. Professional finish for optimal acoustics.',
                'badge_text': 'Framing',
                'badge_color': 'warning',
                'image_name': 'warehouse-framing-2.jpg',
                'is_hero': True
            },
            {
                'title': 'Custom Dome Ceiling',
                'description': 'Architectural specialty work with curved design elements. A centerpiece that transforms any space.',
                'badge_text': 'Specialty Work',
                'badge_color': 'primary',
                'image_name': 'dome-ceiling.jpg'
            },
            {
                'title': 'Metal Framing & Insulation',
                'description': 'Complete wall systems with energy-efficient insulation. Building foundations for lasting renovations.',
                'badge_text': 'Framing',
                'badge_color': 'success',
                'image_name': 'drywall-framing.jpg'
            },
            {
                'title': 'Sports Facility Renovation',
                'description': 'Complete interior transformation with custom graphics. Created an inspiring athletic environment.',
                'badge_text': 'Renovation',
                'badge_color': 'info',
                'image_name': 'sports-wall.jpg'
            },
            {
                'title': 'Modern Ceiling Design',
                'description': 'Curved architectural elements with integrated lighting. Contemporary design meets functional excellence.',
                'badge_text': 'Modern Design',
                'badge_color': 'secondary',
                'image_name': 'finished-ceiling.jpg'
            },
            {
                'title': 'Large Scale Construction',
                'description': '25,000 sq ft warehouse build-out. From bare structure to functional space.',
                'badge_text': 'Commercial',
                'badge_color': 'danger',
                'image_name': 'warehouse-framing.jpg'
            },
            {
                'title': 'Ceiling Grid Installation',
                'description': 'Professional acoustical ceiling system for commercial office space.',
                'badge_text': 'Ceiling',
                'badge_color': 'primary',
                'image_name': 'ceiling-grid-1.jpg'
            },
            {
                'title': 'Bathroom Ceiling Work',
                'description': 'Moisture-resistant ceiling installation with precision and care.',
                'badge_text': 'Bathroom',
                'badge_color': 'success',
                'image_name': 'bathroom-ceiling.jpg'
            },
            {
                'title': 'Gallery Wall Installation',
                'description': 'Professional drywall installation and finishing for art gallery space.',
                'badge_text': 'Gallery',
                'badge_color': 'warning',
                'image_name': 'gallery-wall.jpg'
            },
            {
                'title': 'Hallway Renovation',
                'description': 'Complete hallway transformation with professional finishing and paint.',
                'badge_text': 'Renovation',
                'badge_color': 'info',
                'image_name': 'hallway-finished.jpg'
            },
            {
                'title': 'Curved Ceiling Detail',
                'description': 'Precision framing for curved architectural elements.',
                'badge_text': 'Detail Work',
                'badge_color': 'secondary',
                'image_name': 'curved-ceiling-detail.jpg'
            },
            {
                'title': 'Warehouse Partition',
                'description': 'Commercial partition walls for warehouse separation.',
                'badge_text': 'Commercial',
                'badge_color': 'danger',
                'image_name': 'warehouse-partition.jpg'
            },
        ]

        locations = [
            'Arlington, VA',
            'Washington, DC',
            'Alexandria, VA',
            'Fairfax, VA',
            'Tysons Corner, VA',
            'Bethesda, MD',
            'Silver Spring, MD',
            'Rockville, MD',
            'McLean, VA',
            'Reston, VA',
            'Falls Church, VA',
            'Annandale, VA',
        ]

        for i, proj_data in enumerate(projects_data):
            image_path = f'projects/gallery/{proj_data["image_name"]}'

            # Check if the image file exists
            full_image_path = os.path.join(settings.MEDIA_ROOT, image_path)
            if not os.path.exists(full_image_path):
                self.stdout.write(self.style.WARNING(f'Image not found: {proj_data["image_name"]}'))
                image_path = ''  # Set to empty if image doesn't exist

            project = Project.objects.create(
                title=proj_data['title'],
                description=proj_data['description'],
                service=random.choice(services),
                location=locations[i % len(locations)],
                completion_date=timezone.now().date() - timedelta(days=random.randint(30, 365)),
                is_featured=(i < 6),  # First 6 are featured
                badge_text=proj_data['badge_text'],
                badge_color=proj_data['badge_color'],
                image=image_path if image_path else '',
                is_hero=proj_data.get('is_hero', False),
                order=i  # Set display order
            )
            self.stdout.write(f'Created project: {project.title} with image: {proj_data["image_name"]}')

        # Create Testimonials
        testimonials_data = [
            {
                'name': 'Sarah Johnson',
                'role': 'Property Manager',
                'content': 'PROS Construction transformed our office space beyond expectations. Professional, on-time, and the quality is outstanding. Highly recommend!',
                'rating': 5,
                'service': services[0]
            },
            {
                'name': 'Michael Chen',
                'role': 'Restaurant Owner',
                'content': 'Excellent work on our restaurant renovation. They minimized disruption to our business and delivered amazing results.',
                'rating': 5,
                'service': services[2]
            },
            {
                'name': 'Amanda Williams',
                'role': 'Homeowner',
                'content': 'The team was professional, clean, and efficient. Our home looks incredible after the complete remodel. Worth every penny!',
                'rating': 5,
                'service': services[1]
            },
            {
                'name': 'David Martinez',
                'role': 'Office Manager',
                'content': 'Great experience from start to finish. Fair pricing, excellent communication, and top-quality work.',
                'rating': 5,
                'service': services[3]
            },
            {
                'name': 'Lisa Thompson',
                'role': 'Store Owner',
                'content': 'They completed our retail renovation ahead of schedule and under budget. Extremely satisfied with the results!',
                'rating': 5,
                'service': services[2]
            }
        ]

        for data in testimonials_data:
            testimonial = Testimonial.objects.create(**data)
            self.stdout.write(f'Created testimonial from: {testimonial.name}')

        self.stdout.write(self.style.SUCCESS('Successfully loaded all sample data with images!'))
