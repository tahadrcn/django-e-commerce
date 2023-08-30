from django.contrib import admin
from .models import company,customer,product,blog,ContactForm

# Register your models here.

admin.site.register(customer)
admin.site.register(company)
admin.site.register(product)
admin.site.register(blog)
admin.site.register(ContactForm)



