from django.contrib import admin
from django.contrib import admin
from .models import JobListing


# Register your models here.
@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'description')
