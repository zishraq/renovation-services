from django.core.management.base import BaseCommand
from services.models import Service, Project, Testimonial
from django.utils import timezone
from datetime import timedelta
import random


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

        # Create Projects
        project_titles = [
            'Modern Office Renovation',
            'Luxury Home Remodel',
            'Restaurant Interior Update',
            'Medical Clinic Expansion',
            'Retail Store Renovation',
            'Residential Kitchen Upgrade',
            'Commercial Space Buildout',
            'Apartment Complex Refresh',
            'Corporate Headquarters Update'
        ]

        locations = [
            'Downtown Manhattan',
            'Brooklyn Heights',
            'Queens Plaza',
            'Midtown East',
            'Upper West Side',
            'Financial District',
            'Long Island City',
            'Tribeca',
            'Chelsea'
        ]

        for i, title in enumerate(project_titles):
            project = Project.objects.create(
                title=title,
                description=f'Complete renovation including drywall, framing, and painting. This project showcased our ability to transform spaces while maintaining business operations. High-quality finishes and attention to detail throughout.',
                service=random.choice(services),
                location=locations[i % len(locations)],
                completion_date=timezone.now().date() - timedelta(days=random.randint(30, 365)),
                is_featured=i < 6
            )
            self.stdout.write(f'Created project: {project.title}')

        # Create Testimonials
        testimonials_data = [
            {
                'name': 'Sarah Johnson',
                'role': 'Property Manager',
                'content': '\'PROS Construction\' transformed our office space beyond expectations. Professional, on-time, and the quality is outstanding. Highly recommend!',
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

        self.stdout.write(self.style.SUCCESS('Successfully loaded all sample data!'))
