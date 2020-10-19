from django import forms
from . models import Reservation


class ReserveForm(forms.ModelForm):
    # name = models.CharField(max_length=40)
    # email = models.EmailField(max_length=60)
    # phone = models.IntegerField()
    # number_of_persons = models.IntegerField()
    # date = models.DateField()
    # time = models.TimeField()

    # name = forms.CharField(widget=forms.TextInput(attrs={
    #     "type": "email",
    #     "name": "email",
    #     "id": "email",
    #     "placeholder": "Type your email address",
    # }), label="")
    
    class Meta:
        model = Reservation
        fields = "__all__"