from django.forms import ModelForm, Textarea
from reviews.models import CourseReview, AdminMessage


class RecomForm(ModelForm):
    class Meta:
        model = CourseReview
        fields = ['year','cuatr','recom','comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 10}),
        }


class MessageForm(ModelForm):
    class Meta:
        model = AdminMessage
        fields = ['mensaje']
        widgets={
            'mensaje': Textarea(attrs={'cols':40,'rows':10}),
        }
