from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail





def home(request):
    title = "Contact Us"
    form = ContactForm(request.POST or None)
    confirm_message = None

    print form

    if form.is_valid():
        comment = form.cleaned_data['comment']
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        sbj = 'Message from Seven.com'
        msg = '%s %s'  %(comment, name)
        #frm = ['teste@3es.in']
        to_us = ['teste@3es.in']
        print sbj, msg, to_us
        send_mail(sbj, msg, to_us, to_us, fail_silently=False)
        title = "Thank You"
        confirm_message = " Thanks for message "
    else:
        print "FORM INVALID"

    context = {
        'title': title,
        'form': form,
        'confirm_message': confirm_message
        }

    template = "contact.html"

    return render(request,template,context)

