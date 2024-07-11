from django.db import models
from django.contrib.auth.models import User
import uuid

# project table
class project(models.Model):
    crop_choice = (
        ('', 'select'),
        ('NA', 'NA'),
        ('corn', 'corn'),
        ('cotton', 'cotton'),
        ('rice', 'rice'),
        ('fescue', 'fescue'),
        ('sorgum', 'sorgum')
    )
    project_id = models.CharField(max_length=120, primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    project_editors = models.CharField(max_length=100,  default='NA')
    start_year = models.IntegerField(default=2019)
    acesss = models.TextField(default='Na')
    crop = models.CharField(max_length=50, choices=crop_choice, default='NA')
    funding_source = models.CharField(max_length=100, default='Unknown')
    metadata = models.TextField(default='No metadata available')


    def __str__(self):
        return self.project_id
    

# location information table
class Location(models.Model):
    location_id = models.CharField(max_length=100, primary_key=True)
    year_added = models.CharField(max_length=100, default='Unknown')
    plot_boundary = models.CharField(max_length=100, default='Unknown')
    grids_id = models.CharField(max_length=100, default='Unknown')
    state_id = models.CharField(max_length=100, default='Unknown')
    county_id = models.CharField(max_length=100, default='Unknown')
    latitude = models.CharField(max_length=100, default='Unknown')
    longitude = models.CharField(max_length=100, default='Unknown')
    contact_info= models.CharField(max_length=100, default='Unknown')

    def __str__(self):
        return self.location_id

# Weather Table
class weather(models.Model):
    weather_id = models.CharField(max_length=100, primary_key=True)
    location_id = models.CharField(max_length=100, default='Unknown')

    def __str__(self):
        return self.weather_id

# Soil profile table
class soil_profile(models.Model):
    soil_id = models.CharField(max_length=100, primary_key=True)
    location_id = models.CharField(max_length=100, default='Unknown')

    def __str__(self):
        return self.soil_id
    
# experement table
class experements(models.Model):
    experement_id = models.CharField(max_length=100, primary_key=True)
    project_id = models.CharField(max_length=100, default='Unknown')
    location_id = models.CharField(max_length=100, default='Unknown')
    year = models.CharField(max_length=100, default='Unknown')
    planting_date = models.CharField(max_length=100, default='Unknown')
    
    pix_source_1 = models.CharField(max_length=100, default='Unknown')
    pix_rate_1 = models.CharField(max_length=100, default='Unknown')
    pix_timing_1 = models.CharField(max_length=100, default='Unknown')
    pix_source_2 = models.CharField(max_length=100, default='Unknown')
    pix_rate_2 = models.CharField(max_length=100, default='Unknown')
    pix_timing_2 = models.CharField(max_length=100, default='Unknown')
    pix_source_3 = models.CharField(max_length=100, default='Unknown')
    pix_rate_3 = models.CharField(max_length=100, default='Unknown')
    pix_timing_3 = models.CharField(max_length=100, default='Unknown')

    n_source_1 = models.CharField(max_length=100, default='Unknown')
    n_timing_1 = models.CharField(max_length=100, default='Unknown')
    n_rate_1 = models.CharField(max_length=100, default='Unknown')
    n_source_2 = models.CharField(max_length=100, default='Unknown')
    n_timing_2 = models.CharField(max_length=100, default='Unknown')
    n_rate_2 = models.CharField(max_length=100, default='Unknown')
    n_source_3 = models.CharField(max_length=100, default='Unknown')
    n_timing_3 = models.CharField(max_length=100, default='Unknown')
    n_rate_3 = models.CharField(max_length=100, default='Unknown')

    defoliation_1 = models.CharField(max_length=100, default='Unknown')
    defoliation_2 = models.CharField(max_length=100, default='Unknown')
    defoliation_3 = models.CharField(max_length=100, default='Unknown')
    uav_raw = models.CharField(max_length=100, default='Unknown')
    satellite_raw = models.CharField(max_length=100, default='Unknown')
    uav_orthomosiac_RGB = models.CharField(max_length=100, default='Unknown')
    uav_orthomosiac_MS = models.CharField(max_length=100, default='Unknown')
    uav_dsm = models.CharField(max_length=100, default='Unknown')
    metadata = models.CharField(max_length=100, default='Unknown')

    def __str__(self):
        return self.experement_id