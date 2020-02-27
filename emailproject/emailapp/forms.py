from django import forms
from django.forms import widgets

class Subscribe(forms.Form):
	# CHOICES =( 
	# 		("1", "One"), 
	# 	    ("2", "Two"), 
	# 	    ("3", "Three"), 
	# 	    ("4", "Four"), 
	# 	    ("5", "Five"), 
	# 		)
	Email = forms.EmailField(label = 'Recipient Email')
	# choice = forms.ChoiceField(choices = CHOICES, label = 'Choose any one')
	sub = forms.CharField(label = 'Subject')
	body = forms.CharField(label = 'Message', widget=widgets.Textarea)
	attachment = forms.FileField(label = 'Attachment')


	def __init__(self, *args, **kwargs):
		super(Subscribe, self).__init__(*args, **kwargs)
		self.fields['Email'].widget.attrs.update({'class':'emailField'})