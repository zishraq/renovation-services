from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Service, Project, Testimonial
from .forms import ContactForm


def index(request):
    featured_services = Service.objects.filter(is_featured=True)[:3]
    recent_projects = Project.objects.filter(is_featured=True)[:6]
    testimonials = Testimonial.objects.filter(is_active=True)[:3]

    hero_project = Project.objects.filter(is_hero=True).first()

    print(hero_project)

    context = {
        'featured_services': featured_services,
        'recent_projects': recent_projects,
        'testimonials': testimonials,
        'hero_project': hero_project
    }
    return render(request, 'index.html', context)


def services_list(request):
    services = Service.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'services.html', context)


def gallery(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'gallery.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! We\'ll contact you within 24 hours.')
            return redirect('contact')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)


def about(request):
    return render(request, 'about.html')
