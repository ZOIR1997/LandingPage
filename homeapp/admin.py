from django.contrib import admin
from .models import Customer, About, Skills, Expericence, Email, Service, Categories, Images, Testimonial, Contact, Development

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname']
    list_filter = ['fullname']
    search_fields = ['id', 'phone_number', 'fullname']

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'degree', 'email']
    list_filter = ['id']
    search_fields = ['id', 'phone']

@admin.register(Development)
class DevelopmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ['id','programm', 'development_id']
    search_fields = ['programm']

@admin.register(Expericence)
class ExpericenceAdmin(admin.ModelAdmin):
    list_display = ['id', 'programmer', 'company']
    list_filter = ['programmer']
    search_fields = ['id', 'programmer', 'company']

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'programming']
    list_filter = ['programming']
    search_fields = ['id', 'programming']



@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']

@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_id']
    list_filter = ['category_id']
    search_fields = ['id', 'category_id', 'image']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'profession']
    list_filter = ['fullname']
    search_fields = ['id', 'fullname']
    ordering = ['id']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email_contact', 'subject', 'message']
    list_filter = ['name']
    search_fields = ['id', 'name']
    ordering = ['id']