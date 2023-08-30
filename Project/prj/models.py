from django.db import models

class product(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_image = models.TextField()
    product_description = models.TextField()

    def __str__(self):
        return f"{self.product_name}"

class company(models.Model):
    company_name = models.CharField(max_length=100)
    company_logo = models.TextField()
    company_address = models.TextField()
    company_tel = models.CharField(max_length=11)
    company_mail = models.EmailField()
    def __str__(self):
        return f"{self.company_name}"

class customer(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_address = models.TextField()
    customer_mail = models.EmailField()
    customer_tel = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.customer_name}"

class blog(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_description = models.TextField()
    blog_date = models.DateField()

    def __str__(self):
        return f"{self.blog_title}"


class ContactForm(models.Model):
    name = models.CharField("İsim Soyisim", max_length=150)
    email = models.EmailField("Email Adresi", max_length=150)
    subject = models.CharField("Konu", max_length=300)
    message = models.TextField("Mesaj", max_length=2000)
    created_at = models.DateTimeField("Gönderilme Tarihi", auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "İletişim Mesajları"
        verbose_name = "İletişim Mesajı"
