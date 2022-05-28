from modeltranslation.translator import TranslationOptions, register

from . import models


@register(models.User)
class UserTranslationOptions(TranslationOptions):
    fields = ("first_name", "last_name", "citizenship", "city", "description")


@register(models.Skills)
class SkillsTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(models.WorkExperience)
class WorkExperienceTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(models.Education)
class EducationTranslationOptions(TranslationOptions):
    fields = ("institute", "faculty", "specialization")


@register(models.Languages)
class LanguagesTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(models.Portfolio)
class PortfolioTranslationOptions(TranslationOptions):
    fields = ("title", "short_description", "body")
