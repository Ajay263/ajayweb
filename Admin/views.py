from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from .models import Portfolio,SkillS_details,Portfolio_details,Contacts_summary,Facts,Skills,Summary,Education,Professional_Experience,Services,About,Testimonials,Contact
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm



#VIEWS FOR A DetailPAGE(index)
def details(request,id):
    obj = get_object_or_404(Portfolio,pk=id)
    return render(request,'details.html',{'obj':obj})



def index(request):
    obj10 = Contact.objects.all()
    obj12 = Contacts_summary.objects.all()
    obj = Portfolio.objects.all()
    obj2 = Facts.objects.all()
    obj3 = Skills.objects.all()
    obj4 = Summary.objects.all()
    obj5 = Education.objects.all()
    obj6 = Professional_Experience.objects.all()
    obj7 = Services.objects.all()
    obj8 = About.objects.all()
    obj9 = Testimonials.objects.all()
    obj11 = SkillS_details.objects.all()
    obj13= Portfolio_details.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Thank you for contacting us!  We will respond soon!')
            return redirect('index')
    context = {
        'obj': obj,
        'obj2': obj2,
        'obj3': obj3,
        'obj4': obj4,
        'obj5': obj5,
        'obj6': obj6,
        'obj7': obj7,
        'obj13': obj13,
        'obj8': obj8,
        'obj9': obj9,
        'obj11': obj11,
        'obj12': obj12,
        'obj10': obj10,
        'form': form,



    }

    return render(request, 'index.html',context)



