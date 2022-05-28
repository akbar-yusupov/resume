from django import forms
from django.utils.translation import gettext_lazy as _

from . import models


class ContactForm(forms.ModelForm):
    from_whom = forms.CharField(
        label=_("From Whom"),
        min_length=4,
        max_length=64,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": _("Enter site/email"),
            }
        ),
    )
    title = forms.CharField(
        label=_("Title"),
        min_length=4,
        max_length=128,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": _("Enter title"),
            }
        ),
    )
    message = forms.CharField(
        label=_("Message"),
        min_length=4,
        max_length=128,
        widget=forms.Textarea(
            attrs={
                "class": "form-control mb-3",
                "placeholder": _("Enter message"),
                "rows": "3",
                "cols": "5",
            }
        ),
    )

    class Meta:
        model = models.Contact
        fields = "__all__"
