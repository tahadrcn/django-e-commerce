from django.forms import ModelForm

from prj.models import ContactForm
class ContactmeForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = ["name", "email", "subject", "message"]