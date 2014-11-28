from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail





def home(request):
    title = "Contact Us"
    form = ContactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        # comment = form.cleaned_data['comment']
        # name = form.cleaned_data['name']
        # sbj = 'Message from Seven.com'
        # msg = '%s %s '  %(comment, name)
        # frm = form.cleaned_data['email']
        # # to_us = [settings.EMAIL_HOST_USER]
        # print sbj, msg, frm #, to_us
        # send_mail(sbj, msg, frm, ['mail@miguelgomes.eu'], fail_silently=False)

        comment = form.cleaned_data['comment']
        name = form.cleaned_data['name']
        frm  = form.cleaned_data['email']
        sbj = 'Message from Seven.com'
        msg = '%s %s %s'  %(comment, name, frm)
        # #frm = ['teste@3es.in']
        # to_us = ['teste@3es.in']
        # print sbj, msg, to_us
        # send_mail(sbj, msg, to_us, to_us, fail_silently=False)
        send_mail(sbj, msg, 'teste@3es.in', ['mail@miguelgomes.eu'], fail_silently=False)
        title = "Thank You"
        confirm_message = " Thanks for the message "
        form = None


    context = {
        'title': title,
        'form': form,
        'confirm_message': confirm_message
        }

    template = "contact.html"

    return render(request,template,context)

