from django.contrib import admin
from .models import Tag, Project, ProjectImage

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'get_caption')  # Use get_caption method
    readonly_fields = ('image',)

    def get_caption(self, obj):
        return obj.caption
    get_caption.short_description = 'Caption'  # Optional: Set column header

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ('image', 'caption')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', "link", 'created_at', 'updated_at')
    inlines = [ProjectImageInline]
    search_fields = ('title', 'description')
    list_filter = ('tags',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
