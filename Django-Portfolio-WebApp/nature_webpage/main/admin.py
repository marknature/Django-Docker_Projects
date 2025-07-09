from django.contrib import admin
from .models import Tag, Project, ProjectImage

# Register your models here.
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ('image', 'caption')
    readonly_fields = ('image',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', "link", 'created_at', 'updated_at')
    inline = [ProjectImageInline]
    search_fields = ('title', 'description')
    list_filter = ('tags',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Registering the models with the admin site
admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(ProjectImage)
