from django.contrib import admin
from .models import Post
#from post.models import Post -----> üst satırdaki ile aynı işlevi görür.

# Register your models here.


class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'publishing_date', 'slug']
    list_display_links = ['publishing_date']      #burada da title eklemiş olsaydık hata alırdık list_editable ile list_display_links çakışmamamlı
    list_filter = ['publishing_date']
    search_fields = ['title', 'content']
    list_editable = ['title']
    #prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)