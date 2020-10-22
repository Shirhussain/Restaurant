from django import  forms


# I don't wanna use Model form here be cause i didn't use model it self
class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)