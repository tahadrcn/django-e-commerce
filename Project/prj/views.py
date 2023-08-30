from django.shortcuts import render,get_object_or_404

from prj.forms import ContactmeForm
from prj.models import company,customer,product
from django.views.generic.edit import FormView
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings
from cart.cart import Cart

# Create your views here.

def homepage(request):

    return render(request, "homepage.html")

def kahveler(request):
    context = {
        "products" : product.objects.all()
    }
    return render(request, "kahveler.html",context)

def ekipmanlar(request):
    return render(request, "ekipmanlar.html")

def hikayemiz(request):
    return render(request, "hikayemiz.html")

def toptankahve(request):
    return render(request, "toptankahve.html")

def blog(request):
    return render(request, "blog.html")

def iletisim(request):
    return render(request, "iletisim.html")

def product_details(request,id):
    products = product.objects.all()
    selected_urun = None
    for prdct in products:
        if prdct.id == id:
            selected_urun = prdct
    return render(request, "details.html",{
        "prdct" : selected_urun
    })

class ContactFormView(FormView):
    template_name = 'iletisim.html'
    form_class = ContactmeForm
    success_url = '/iletisim'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        email = form.cleaned_data['email']

        mail = EmailMessage(
            f'{name} Tarafından Mesaj Gönderildi',
            f'Konu: {subject}\n\nEmail: {email}\n\nMesaj: {message}\n\n',
            f'"YENİ MESAJ" <{email}>', # email'in kimden (from) geldiğini yazdık.
            [settings.EMAIL_ADMIN], # email'in kime (to) gideceğini belirledik.
            reply_to=[f'{email}'],
        )
        mail.send()
        form.save()
        messages.success(self.request, 'Mesajınız başarıyla gönderildi.')
        return super().form_valid(form)
