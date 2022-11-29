from django import forms
from .models import Topic,Entry

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ['topic_name']
		labels = {'topic_name':''}


class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['content']
		labels = {'content':''}
		widgets = {'text':forms.Textarea(attrs={'cols':80})}
