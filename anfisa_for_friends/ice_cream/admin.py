from django.contrib import admin

from .models import Category, IceCream, Topping, Wrapper

admin.site.empty_value_display = 'Не задано'
admin.site.register(Topping)
admin.site.register(Wrapper)

class IceCreamAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )    
    search_fields = ('title',) 
    list_filter = ('category',)
    list_display_links = ('title',)
    filter_horizontal = ('toppings',)


admin.site.register(IceCream, IceCreamAdmin)

class IceCreamInline(admin.StackedInline):
    model = IceCream
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',        
    )

admin.site.register(Category, CategoryAdmin) 