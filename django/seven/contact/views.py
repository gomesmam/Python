from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail





def home(request):
    form = ContactForm(request.POST or None)

    comment = form.cleaned_date['comment']
    name = form.cleaned_date['name']
    sbj = 'Message from Seven.com'
    msg = '%s %s '  %(comment, name)
    frm = form.cleaned_date['email']
    to_us = [settings.EMAIL_HOST_USER]
    print sbj, msg, frm, to_us
    send_mail(sbj, msg, frm, ['mail@miguelgomes.eu'], fail_silently=False)

    if form.is_valid():
        comment = form.cleaned_date['comment']
        name = form.cleaned_date['name']
        sbj = 'Message from Seven.com'
        msg = '%s %s '  %(comment, name)
        frm = form.cleaned_date['email']
        to_us = [settings.EMAIL_HOST_USER]
        print sbj, msg, frm, to_us
        send_mail(sbj, msg, frm,
            to_us, fail_silently=False)
    else:
        print "FORM INVALID"

    context = locals()
    template = "contact.html"

    return render(request,template,context)

