from django import forms
from django.forms import HiddenInput

from app.models import Room, Feedback, Comment


class ProductModelForm(forms.ModelForm):
    user = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Room
        exclude = ()


class FeedbackModelForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ()


class CommentForm(forms.ModelForm):
    user = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Comment
        exclude = ()