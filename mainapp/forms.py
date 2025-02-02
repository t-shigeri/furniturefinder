from django import forms
from .models import RoomPhoto, Furniture

class RoomPhotoForm(forms.ModelForm):
    class Meta:
        model = RoomPhoto
        fields = ['photo']

STYLE_CHOICES = [
        ('modern', 'ソファ'),
        ('classic', '机'),
        ('industrial', '椅子'),
        ('scandinavian', 'ランプ'),
        ('bohemian', 'その他'),
    ]

class FurnitureSearchForm(forms.Form):
    min_height = forms.IntegerField(required=False, label='最小高さ')
    max_height = forms.IntegerField(required=False, label='最大高さ')
    min_width = forms.IntegerField(required=False, label='最小幅')
    max_width = forms.IntegerField(required=False, label='最大幅')
    style = forms.ChoiceField(required=False, choices=STYLE_CHOICES, label='スタイル')

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)