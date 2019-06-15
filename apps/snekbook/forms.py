from django import forms
from django.forms import ValidationError

from .utils import translation

def validate_snek_speak(comment_text):
    try:
        snek_translation = translation.to_snek(comment_text)
    except translation.SnekTranslationImpossible as e:
        raise ValidationError(
            "The following characters are disallowed: %(chars)s",
            params={"chars": e.disallowed_characters},
        )

class CommentForm(forms.Form):
    comment = forms.CharField(
        max_length=100,
        widget=forms.Textarea(attrs={'rows': '2', 'class': 'form-control'}),
        validators=[validate_snek_speak]
    )