from django.shortcuts import render

from .forms import ContactForm

# Create your views here.




def home(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        print request.POST

    context = locals()
    template = "contact.html"

    return render(request,template,context)

