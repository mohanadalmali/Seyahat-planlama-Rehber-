# from django.contrib import admin
# from .models import Service, ServiceDetail
# # Register your models here.

# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ('title') # Admin panelinde görüntülenecek sütunları belirtir
#     fields = ('title', 'description', 'image','show_on_homepage') 



# class ServiceDetailAdmin(admin.ModelAdmin):
#     list_display = ('title') # Admin panelinde görüntülenecek sütunları belirtir
#     fields = ('title', 'description', 'image') 

# admin.site.register(ServiceDetail, ServiceDetailAdmin)
# admin.site.register(Service, ServiceAdmin)


from django.contrib import admin
from .models import Service, ServiceDetail

admin.site.register(Service)
admin.site.register(ServiceDetail)

