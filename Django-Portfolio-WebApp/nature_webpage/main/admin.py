from django.contrib import admin
from .models import Tag, Project, ProjectImage

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'get_caption', 'created_at')
    readonly_fields = ('created_at',)

    def get_caption(self, obj):
        return obj.caption or "No caption"
    get_caption.short_description = 'Caption'

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1 
    fields = ('image', 'caption')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')  # Removed 'technology' field
    inlines = [ProjectImageInline]
    search_fields = ('title', 'description')
    list_filter = ('tags', 'created_at')
    filter_horizontal = ('tags',)  # Better widget for many-to-many
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)