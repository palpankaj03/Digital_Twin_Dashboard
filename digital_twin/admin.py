from django.contrib import admin
from .models import project, weather, soil_profile, experements

# header in admin area 
admin.site.site_header = 'Digital Twin Dashboard'

# adding tabels to admin area
@admin.register(project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'project_id', 'user_id', 
        'project_editors', 'start_year', 'acesss',
        'crop','funding_source', 'metadata'
    )

@admin.register(weather)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'weather_id', 'location_id'
    )

@admin.register(soil_profile)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'soil_id', 'location_id'
    )


@admin.register(experements)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'experement_id','project_id','location_id','year','planting_date',
        'pix_source_1','pix_rate_1','pix_timing_1','pix_source_2','pix_rate_2','pix_timing_2','pix_source_3','pix_rate_3','pix_timing_3',
        'n_source_1','n_timing_1','n_rate_1','n_source_2','n_timing_2','n_rate_2','n_source_3','n_timing_3','n_rate_3',
        'defoliation_1','defoliation_2','defoliation_3','uav_raw','satellite_raw','uav_orthomosiac_RGB','uav_orthomosiac_MS','uav_dsm','metadata'
    )