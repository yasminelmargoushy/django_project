from django import forms
from blog.models import PostReview

class PostReviewForm(forms.ModelForm):
	content= forms.CharField(widget=forms.Textarea(
		attrs={'rows':'4','class': 'md-textarea form-control',
        'placeholder': 'comment here ...',}))


class Meta:
	model=PostReview
	fields=('content',)