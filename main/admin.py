from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from . import models


@admin.register(models.User)
class UserAdmin(TranslationAdmin):
    list_display = (
        "first_name",
        "last_name",
        "job_title",
        "job_status",
        "ready_to_relocate",
    )
    list_editable = ("job_status", "ready_to_relocate")
    list_display_links = (
        "first_name",
        "last_name",
    )


@admin.register(models.Skills)
class SkillsAdmin(TranslationAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(models.WorkExperience)
class WorkExperienceAdmin(TranslationAdmin):
    list_display = ("title", "start", "end")


@admin.register(models.Education)
class EducationAdmin(TranslationAdmin):
    list_display = ("institute", "faculty", "specialization", "is_completed")
    list_editable = ("is_completed",)


@admin.register(models.Languages)
class LanguagesAdmin(TranslationAdmin):
    list_display = ("name", "level")
    list_editable = ("level",)


@admin.register(models.Portfolio)
class PortfolioAdmin(TranslationAdmin):
    list_display = ("title", "short_description", "created_at", "is_active")
    list_editable = ("short_description",)
    list_filter = ("is_active",)
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("technologies",)


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("from_whom", "title", "message", "created_at")
    search_fields = ("from_whom", "title")

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
