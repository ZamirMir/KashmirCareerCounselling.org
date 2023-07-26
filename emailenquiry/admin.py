from django.contrib import admin
from emailenquiry.models import emailEnquiry

# Register your models here.
class EmailForm(admin.ModelAdmin):
    listdisplay=('email')


admin.site.register(emailEnquiry,EmailForm)




