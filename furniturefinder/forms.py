from django import forms

class FurnitureSearchForm(forms.Form):
    min_height = forms.FloatField(required=False, label='最小高さ')
    max_height = forms.FloatField(required=False, label='最大高さ')
    min_width = forms.FloatField(required=False, label='最小幅')
    max_width = forms.FloatField(required=False, label='最大幅')
    style = forms.ChoiceField(required=False, label='スタイル')