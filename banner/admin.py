from django.contrib import admin
from banner.models import Banner
# Register your models here.


class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'visible', 'weight')


admin.site.register(Banner, BannerAdmin)