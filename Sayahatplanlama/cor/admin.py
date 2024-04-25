from django.contrib import admin
from .models import IndexPage, abouts

# IndexPage modelini admin panelinde görüntülemek için bir yönetici sınıfı oluşturun
class IndexPageAdmin(admin.ModelAdmin):
    # Ana sayfa için içerik
    list_display = ('index_title', 'index_description')
    # Hakkımızda için içerik
    fieldsets = (
        ('Ana Sayfa İçeriği', {
            'fields': ('index_title', 'index_image', 'index_description')
        }),
        ('Hakkımızda İçeriği', {
            'fields': ('about_title', 'about_image', 'about_description')
        }),
        ('Neden Bizi Seçmelisiniz İçeriği', {
            'fields': ('why_choose_us_title', 'why_choose_us_description')
        }),
        ('Footer Bilgileri', {
            'fields': ('footer_instagram_link', 'footer_facebook_link','footer_linkled_link','footer_X_link' ,'footer_phone_number', 'footer_email')
        }),
    )
    class Meta:
        model=IndexPage
class AboutsAdmin(admin.ModelAdmin):
    list_display = ('about_titleb', 'about_imageb') # Admin panelinde görüntülenecek sütunları belirtir
    fields = ('about_titleb', 'about_imageb', 'about_descriptionb') # Düzenleme formundaki alanları belirtir
# abouts modelini yönetici paneline kaydet



admin.site.register(abouts, AboutsAdmin)
# IndexPage modelini yönetici paneline kaydet
admin.site.register(IndexPage, IndexPageAdmin)