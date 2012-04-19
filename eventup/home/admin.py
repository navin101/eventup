from home.models import *
from django.contrib import admin

def mark_reported(modeladmin, request, queryset):
    queryset.update(reported=True)
mark_reported.short_description = "Report items (and hide)"

# admin.site.add_action(mark_reported, "Fetch")

