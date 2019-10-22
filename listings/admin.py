from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('title', 'city', 'state', 'zipcode')
    list_per_page = 3


admin.site.register(Listing, ListingAdmin)
