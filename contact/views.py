from django.shortcuts import redirect, render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

from . forms import ContactForm


def send_email(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            #if you are curios about have i get(subject,email and message)
            # in templates go to inspect element and find the input tag, you see the name of each input 
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            form = ContactForm()
            try:
                #shirhussain@admin.af is the receptor of this email
                # send_mail(name,email,phone,message,['shirhussain@admin.af'])
                send_mail(subject, message,from_email, ['no_reply@gmail.com'],fail_silently=False)
                print(send_mail)
            except :
                BadHeaderError("Invalid data, please make sure that you are entring the right data")
            return redirect("contact:send_success")
    else:
        form = ContactForm()

    context = {
        'form':form
    }
    return render(request, "contact/contact.html", context)
    


def send_success(request):
    return HttpResponse("Thanks in advance from your email (^_^)")
