from services.models import *
from django.contrib import admin

#class FeedCategoryAdmin(admin.ModelAdmin):
#    fields = ['name']
#    
#class FeedAdmin(admin.ModelAdmin):
#    fields = ['category', 'name']
#    
#class ContentAdmin(admin.ModelAdmin):
#    fields = ['feed', 'image_url', 'link', 'tag']
#    
#admin.site.register(FeedCategory, FeedCategoryAdmin)
#admin.site.register(Feed, FeedAdmin)
#admin.site.register(Content, ContentAdmin)

admin.site.register(FbUser)
