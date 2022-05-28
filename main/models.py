from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class JobStatusChoices(models.IntegerChoices):
        full_time = 1, _("Full time job")
        part_time = 2, _("Part-time job")
        busy = 3, _("Busy")

    class JobTypeChoices(models.IntegerChoices):
        remote = 1, _("Remote work")
        daily_commute = 2, _("Daily Commute")

    photo = models.ImageField(_("Photo"), upload_to="photo/")
    citizenship = models.CharField(
        _("Citizenship"), default="Uzbekistan", max_length=32
    )
    city = models.CharField(_("City"), default="Tashkent", max_length=32)
    description = RichTextField(_("Description"))
    birth_date = models.DateField(_("Birth Date"), default="2003-12-11")
    job_title = models.CharField(
        _("Job Title"), max_length=128, default="Python backend developer"
    )
    job_status = models.IntegerField(
        _("Job Status"), choices=JobStatusChoices.choices, default=1
    )
    job_type = models.IntegerField(
        _("Job Type"), choices=JobTypeChoices.choices, default=1
    )
    ready_to_relocate = models.BooleanField(
        _("Ready To Relocate"), default=False
    )

    def save(self, *args, **kwargs):
        self.pk = self.id = 1
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


class Skills(models.Model):
    name = models.CharField(_("Name"), max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Skill")
        verbose_name_plural = _("Skills")


class WorkExperience(models.Model):
    start = models.DateField(_("Start date"))
    title = models.CharField(_("Title"), max_length=128)
    description = RichTextField(_("Description"))
    end = models.DateField(_("End date"), null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.start < self.end:
            super().save(*args, **kwargs)
        else:
            raise ValidationError(_("The start date should be earlier than end date"))

    class Meta:
        verbose_name = _("Work Experience")
        verbose_name_plural = _("Work Experience")
        ordering = ("start",)


class Education(models.Model):
    institute = models.CharField(_("Institute"), max_length=128)
    faculty = models.CharField(_("Faculty"), max_length=128)
    specialization = models.CharField(_("Specialization"), max_length=128)
    is_completed = models.BooleanField(_("Is Completed"), default=True)

    def __str__(self):
        return self.institute

    class Meta:
        verbose_name = _("Education")
        verbose_name_plural = _("Education")


class Languages(models.Model):
    class LevelChoices(models.IntegerChoices):
        beginner = 1, _("beginner")
        pre_intermediate = 2, _("pre-intermediate")
        intermediate = 3, _("intermediate")
        upper_intermediate = 4, _("upper intermediate")
        native = 5, _("native speaker")

    name = models.CharField(_("Name"), max_length=128)
    level = models.IntegerField(
        _("Level"), default=1, choices=LevelChoices.choices
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Language")
        verbose_name_plural = _("Languages")


class Portfolio(models.Model):
    title = models.CharField(_("Title"), max_length=128)
    short_description = models.CharField(_("Short Description"), max_length=64)
    body = RichTextField(_("Body"), blank=True, null=True)
    image = models.ImageField(_("Image"), upload_to="portfolio/")
    technologies = models.ManyToManyField(
        Skills, verbose_name=_("Technologies")
    )
    slug = models.SlugField(_("Slug"), unique=True, max_length=32)
    created_at = models.DateField(_("Created at"))
    is_active = models.BooleanField(_("Is Active"), default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("main:portfolio-detail", args=[self.slug])

    class Meta:
        verbose_name_plural = _("Portfolio")
        verbose_name = _("Portfolio")
        ordering = ("created_at",)


class Contact(models.Model):
    from_whom = models.CharField(_("From Whom"), max_length=64)
    title = models.CharField(_("Title"), max_length=128)
    message = models.TextField(_("Message"), max_length=1024)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)

    def __str__(self):
        return self.from_whom

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")
