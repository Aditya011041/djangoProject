from django.contrib import admin
from app.models import UserData, ArticleData

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'word_counts', 'status', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('status', )
    date_hierarchy = 'created_at'
    ordering = ('created_at',)
    readonly_fields = ('word_counts', 'created_at', 'updated_at')
    
admin.site.register(UserData)
admin.site.register(ArticleData, ArticleAdmin)
