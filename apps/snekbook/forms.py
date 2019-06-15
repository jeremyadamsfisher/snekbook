from django import forms
from django.forms import ValidationError

from . import utils

def validate_snek_speak(comment_text):
    if not set(comment_text).issubset("Ss !,."):
        raise ValidationError(
            "The following characters are disallowed: %(chars)s",
            params={"chars": list(set(comment_text).difference(set("Ss !,.")))},
        )

class CommentForm(forms.Form):
    comment = forms.CharField(
        max_length=100,
        widget=forms.Textarea(attrs={'rows': '2', 'class': 'form-control'}),
        #validators=[validate_snek_speak]
    )