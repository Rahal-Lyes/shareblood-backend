from django.contrib import admin

from accounts.models import CustomUser
from shop.models import Category,Product

admin.site.register(CustomUser)



class CategoryAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}
  list_display = ("name", "slug")

class ProductAdmin(admin.ModelAdmin):
  prepopulated_fields= {'slug':('product_name',)}
  list_display =( "product_name","slug")


admin.site.register(Product,ProductAdmin)
admin.site.register(Category, CategoryAdmin)
