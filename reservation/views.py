from django.shortcuts import render
from . models import Reservation
from . forms import ReserveForm

def reserve_table(request):
    reserveation_form = ReserveForm()
    if request.method == "POST":
        reserveation_form = ReserveForm(request.POST)
        if reserveation_form.is_valid():
            reserveation_form.save()

    context = {
        'form':reserveation_form
    }
    
    return render(request, "reservation/reservation.html", context)

