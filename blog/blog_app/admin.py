from django.contrib import admin
from .models import Article,Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at',)

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at','update_at')

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id

        obj.save()
    
    

admin.site.register(Article,ArticleAdmin)
admin.site.register(Category,CategoryAdmin)
