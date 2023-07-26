from django.contrib import admin
from contactenquiry.models import contactEnquiry

# Register your models here.
class ContactForm(admin.ModelAdmin):
    list_display=('name','email','phone_number','message')


admin.site.register(contactEnquiry,ContactForm)
