import email
import re
from time import sleep
from django.shortcuts import redirect, render
from user.models import Customer
from user.forms import CustomerForm
from django.http import HttpResponse

from django.core.mail import send_mail

#for html email start here
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
#for html email end here

# Create your views here.
def myhome(request):
    return render(request, "user/homepage.html")


def menus(request):
    return render(request, "user/menus.html")

def packagegold(request):
    return render(request, "user/packagegold.html")

def packagesilver(request):
    return render(request, "user/packagesilver.html")

def packageplatinum(request):
    return render(request, "user/packageplatinum.html")


def whatsappdata(mno, msg):
    import time
    import webbrowser as web
    import pyautogui as pg
    mobileno = "+91"+mno
    web.open('https://web.whatsapp.com/send?mobileno='+mobileno+'&text='+msg)
    time.sleep(30)
    
    pg.press('enter')
    
    pg.click('enter')

'''def sendMassEmail(request,emailto):
   msg1 = ('noreply', 'Thank you for choosing Jaswik Cateres for your beutiful event...as soon as possible we will contact to you', 'balajikaragir07@gmail.com', [emailto])
   msg2 = ('noreply', 'Thank you for choosing Jaswik Cateres for your beutiful event...as soon as possible we will contact to you', 'balajikaragir07@gmail.com', [emailto])
 
   #msg2 = ('subject 2', 'message 2', 'polo@polo.com', [emailto2])
   res = send_mass_mail((msg1, msg2), fail_silently = False)
   return HttpResponse('%s'%res)'''


    
    


def contactus(request):
    try:

        if request.method == 'POST':
            studForm = CustomerForm(request.POST)
            print("POST")
            if studForm.is_valid():
                print("Valid data")
                n = studForm.cleaned_data['name']
                mno = studForm.cleaned_data['mobileno']
                eml = studForm.cleaned_data['email']
                msg = studForm.cleaned_data['message']
                print(n + " "+mno+" "+eml+" "+msg)
                
                #sendMassEmail(request,eml)
                #sendSimpleEmail(request,eml)
                send_mail(
                'noreplyjaswikcaterers',
                'Dear '+n+',\nThank you for choosing Jaswik Cateres for your great event... I have received your Enquiry..as soon as possible we will contact to you\n\n\n\n Thanks and regards,\n Jaswik Caterers\n Mobile no: 9604802874\n email: jaswikcaterersno1@gmail.com ',
                'balajikaragir07@gmail.com',
                [eml],
                fail_silently=False,
                )

                send_mail(
                'enquiry',
                'ENQUIRY \n\n Name:'+n+'\n Mobile no:'+mno+'\n Email:'+eml+'\n Message:'+ msg+'',
                'balajikaragir07@gmail.com',
                ['karagirbalaji992@gmail.com'],
                fail_silently=False,
                )
                #whatsappdata(mno,msg)
                #successmsg = "Message has successufully sent..."
            # print(successmsg)
                # insert
                rec = Customer(name=n, mobileno=mno, email=eml, message=msg)
                rec.save()

                # update
                #rec = Student(2,name=n,roll=r,per=p)
                # rec.save()

                # delete

                print("Record Inserted Successfully")
                #return redirect('customerinfo')
                return redirect('contactus')

                #return render(request,'customerinfo',{'successmsg':successmsg})
            else:
                print("Invalid data")
        else:
            studForm = CustomerForm()
            print("GET")
            #rec = Customer(name=n,mobileno=mno,email=eml,message=msg)
            # rec.save()
            # return redirect('customerinfo')
        return render(request, "user/contactus.html", locals())
        # ret
        # urn render(request, "user/contactus.html")
    except Exception as e:
        raise e


def quatation(request):
    return render(request, "user/quatation.html")


def ourservices(request):
    return render(request, "user/ourservices.html")


def gallary(request):
    return render(request, "user/gallary.html")


def termsandconditions(request):
    return render(request, "user/termsandconditions.html")


def aboutus(request):
    return render(request, "user/aboutus.html")


def mycustomer(request):
    stud = Customer.objects.all()
    return render(request, "user/customerinfo.html", locals())


'''def newcustomer(request):
    if request.method == 'POST':
        studForm = CustomerForm(request.POST)
        print("POST")
        if studForm.is_valid():
            print("Valid data")
            n = studForm.cleaned_data['name']
            mno = studForm.cleaned_data['mobileno']
            eml=studForm.cleaned_data['email']
            msg=studForm.cleaned_data['message']

            
            #insert
            rec = Customer(name=n,mobileno=mno,email=eml,message=msg)
            rec.save()
            
            #update
            #rec = Student(2,name=n,roll=r,per=p)
            #rec.save()
            
            #delete
            
            
            print("Record Inserted Successfully")
            return redirect('customerinfo')
        else:
            print("Invalid data")
    else:
        studForm = CustomerForm()
        print("GET")
    return render(request, "user/contactus.html",locals())'''
