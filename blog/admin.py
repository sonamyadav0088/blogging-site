from django.contrib import admin


from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'details']
    prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Blog, BlogAdmin)




