from django.contrib import admin
from .models import Portfolio,SkillS_details,Portfolio_details,Contacts_summary,Facts,Skills,Summary,Education,Professional_Experience,Services,About,Contact,Testimonials

from django.contrib import admin
from .models import Contact_form1

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'date']

admin.site.register(Contact_form1, ContactAdmin)

# Register your models here.

admin.site.register(Portfolio)
admin.site.register(Facts)
admin.site.register(Skills)
admin.site.register(Summary)
admin.site.register(Education)
admin.site.register(Professional_Experience)
admin.site.register(Services)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Testimonials)
admin.site.register(SkillS_details)
admin.site.register(Portfolio_details)
admin.site.register(Contacts_summary)



