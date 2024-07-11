from django.contrib import admin
from .models import Post, Publicite

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "created_on")
    list_filter = ("status", "created_on")
    search_fields = ("title", "content")
    
class PubAdmin(admin.ModelAdmin):
    list_display = ("titre", "url")

admin.site.register(Post, PostAdmin)
admin.site.register(Publicite, PubAdmin)
