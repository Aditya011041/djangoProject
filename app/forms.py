from django import forms

ARTICLE_STATUS = (
    ('draft', 'draft'),
    ('inprogress', 'in progress'),
    ('published', 'published'),
)

class CreateArticleForm(forms.Form):
    title = forms.CharField(max_length=100)
    status = forms.ChoiceField(choices=ARTICLE_STATUS)
    content = forms.CharField(widget=forms.Textarea, required=False)
    word_counts = forms.IntegerField()
    twitter_post = forms.CharField(widget=forms.Textarea, required=False)
    