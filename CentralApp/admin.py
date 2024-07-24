from django.contrib import admin
from .models import CampusAVS, CampusAVSReport, ReportImage, HistoryImage
# Register your models here.

admin.site.site_header = 'AFCF AGM PORTAL'


@admin.register(CampusAVS)
class CampusAVSAdmin(admin.ModelAdmin):
    list_display = ['campusOrSchoolAcronym', 'institutionType','campusName', 'averageNumberOfStudent', 'numberOfWorkforce', 'last_edited']
    search_fields = ['campusOrSchoolAcronym', 'campusName', 'institutionType']

@admin.register(CampusAVSReport)
class CampusAVSReportAdmin(admin.ModelAdmin):
    list_display = ['campusOrSchoolAcronym', 'program_type', 'year']
    search_fields = ['campusOrSchoolAcronym', 'program_type']

@admin.register(ReportImage)
class ReportImageAdmin(admin.ModelAdmin):
    list_display = ['campusOrSchoolAcronym', 'program_type']
    search_fields = ['campusOrSchoolAcronym', 'program_type']

@admin.register(HistoryImage)
class HistoryImageAdmin(admin.ModelAdmin):
    list_display = ['campusOrSchoolAcronym', 'id']
    search_fields = ['campusOrSchoolAcronym',]

