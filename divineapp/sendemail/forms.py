from django import forms
import re

def validate_comment_word_count(value):
      count = len(value.split())
      if count < 30:
            raise forms.ValidationError(('Please provide at least a 30 word message, %(count)s words is not descriptive enough'),
                                        params={'count': count},)

class ContactForm(forms.Form):
      name = forms.CharField(required=True)
      email = forms.EmailField(label='Your email')
      comment = forms.CharField(widget=forms.Textarea,validators=[validate_comment_word_count],error_messages={"required":"Please, pretty please provide a comment"})
      field_order=['email','name','comment']
      def __init__(self, *args, **kwargs):
          #super(ContactForm, self).__init__(*args, **kwargs)
            initial_arguments = kwargs.get('initial', None)
            updated_initial = initial_arguments
            if initial_arguments:
                  user = initial_arguments.get('user',None)
                  if user:
                        updated_initial['name'] = getattr(user, 'first_name', None)
                        updated_initial['email'] = getattr(user, 'email', None)
            kwargs.update(initial=updated_initial)
            super(ContactForm, self).__init__(*args, **kwargs)
      def clean(self):
            super(ContactForm, self).clean()
            name = self.cleaned_data.get('name','')
            email = self.cleaned_data.get('email','')
            if name.lower() not in email:
                  message = "Please provide an email that contains your name, or viceversa"
                  #self.add_error('name', message)
                  #self.add_error('email', forms.ValidationError(message))
                  self.add_error(None, message)
                  #raise forms.ValidationError("Please provide an email that contains your name, or viceversa")
      def clean_name(self):
            # Get the field value from cleaned_data dict
            value = self.cleaned_data['name']
            # Check if the value is all upper case
            if value.isupper():
                  # Value is all upper case, raise an error
                  raise forms.ValidationError("Please don't use all upper case for your name, use lower case",code='uppercase')
            # Always return value
            return value
      def clean_email(self):
      	    # Get the field value from cleaned_data dict
            value = self.cleaned_data['email']
	    # Check if the value end in @hotmail.com
            if value.endswith('@hotmail.com'):
                  # Value ends in @hotmail.com, raise an error
                  raise forms.ValidationError("Please don't use a hotmail email, we simply don't like it",code='hotmail')
            # Always return value
            return value
