from django.shortcuts import render

# Create your views here.
# views.py

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

from django.shortcuts import render
from .models import JobListing  # Import your JobListing model

def search_jobs(request):
    title = request.GET.get('title')
    location = request.GET.get('location')

    if title and location:
        job_listings = JobListing.objects.filter(title__icontains=title, location__icontains=location)
    elif title:
        job_listings = JobListing.objects.filter(title__icontains=title)
    elif location:
        job_listings = JobListing.objects.filter(location__icontains=location)
    else:
        job_listings = []

    context = {
        'job_listings': job_listings,
    }

    return render(request, 'search_results.html', context)  # Replace 'search_results.html' with your actual template name

