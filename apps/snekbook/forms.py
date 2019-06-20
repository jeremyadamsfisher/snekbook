from django import forms
from django.forms import ValidationError

from . import utils


def validate_snek_speak(comment_text):
    try:
        utils.translation.to_snek(comment_text)
    except utils.translation.SnekTranslationImpossible as translation_exception:
        raise ValidationError(
            "The following characters are disallowed: %(chars)s",
            params={"chars": translation_exception.disallowed_characters},
        )


class CommentForm(forms.Form):
    comment = forms.CharField(max_length=100, validators=[validate_snek_speak])
