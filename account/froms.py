from haminjory.models import Article
from django import forms

class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model=Article
        fields='__all__'