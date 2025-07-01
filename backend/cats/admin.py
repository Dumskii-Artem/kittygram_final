from django.contrib import admin
from .models import Cat, Achievement, AchievementCat


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'color', 'birth_year')
    search_fields = ('name',)
    list_filter = ('color',)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(AchievementCat)
class AchievementCatAdmin(admin.ModelAdmin):
    list_display = ('achievement', 'cat')


admin.site.register(Cat)
admin.site.register(Achievement)
admin.site.register(AchievementCat)
