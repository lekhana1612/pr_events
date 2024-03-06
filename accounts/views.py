from django import forms
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound,JsonResponse
from feedback.models import feedback

from django.core.mail import EmailMessage
from django.conf import settings
from django.core.mail import send_mail
import uuid
from customerdata.models import customerdata
from customerdata.forms import CustomerForm
from django.utils.html import strip_tags
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from payment.forms import PaymentForm
from gallery.models import Decoration
from payment.models import payment
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from remainingAmt.models import AdvanceAmount

 # Adjust the length as needed


# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')


#this is for book for new event page
def saveenquiry(request):
    if request.method=="POST":
        customer_id = str(uuid.uuid4())[:4]
    
        customername=request.POST.get('customername')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        eventdate=request.POST.get('eventdate')
        eventname=request.POST.get('eventname')
        eventvenue=request.POST.get('eventvenue')
        eventcity=request.POST.get('eventcity')
        pincode=request.POST.get('pincode')
        quotation=request.POST.get('quotation')
        advance=request.POST.get('advance')
        balance=request.POST.get('balance')
        description=request.POST.get('description')
        form=customerdata(customer_id=customer_id,customername=customername,phone=phone,email=email,eventdate=eventdate,eventname=eventname,eventvenue=eventvenue,eventcity=eventcity,pincode=pincode,quotation=quotation,advance=advance,balance=balance,description=description)
        
        
        form.save()
        form='data inserted'
        

        admin_email = settings.ADMIN_EMAIL
        email_subject_admin = 'New Booking Received'
        email_template_admin = 'admin_email.html'
        email_context_admin = {'customer_id':customer_id,'customername':customername,'phone':phone,'email':email,'eventdate':eventdate,'eventname':eventname,'eventvenue':eventvenue,'eventcity':eventcity,'pincode':pincode,'quotation':quotation,'advance':advance,'balance':balance,'description':description}
        email_body_admin = render_to_string(email_template_admin, email_context_admin)
        plain_email_body_admin = strip_tags(email_body_admin)

        send_mail(
                email_subject_admin,
                plain_email_body_admin,
                settings.EMAIL_HOST_USER,
                [admin_email],
                html_message=email_body_admin)
      
        
        email_subject = 'Your Booking Confirmation'
        email_template = 'customer_email.html'
        email_from=settings.EMAIL_HOST_USER
        recipient_list=[email]
        
        
        email_context = {'customer_id':customer_id,'customername':customername,'phone':phone,'email':email,'eventdate':eventdate,'eventname':eventname,'eventvenue':eventvenue,'eventcity':eventcity,'pincode':pincode,'quotation':quotation,'advance':advance,'balance':balance,'description':description}
        email_body = render_to_string(email_template,email_context)
        plain_email_body = strip_tags(email_body)
        send_mail(email_subject,plain_email_body,settings.EMAIL_HOST_USER,recipient_list,
                  html_message=email_body)
        return redirect('image_template')
    else:
        form=CustomerForm
        return render(request,'home.html',{'form':form})
    
def image_template(request):
    return render (request,'image_template.html')


        #send_mail('The contact form subject','This is the message',['prevents02@gmail.com'],html_message=html)
        

        
      
    

 


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')


        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('client')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def feedback(request):
    
    return render (request,'feedback.html')



def gallery(request):
    return render (request,'gallery.html')
def about(request):
    return render (request,'about.html')
def logout(request):
    return render (request,'logout.html')
def register_email(request):
    return render (request,'register_email.html')
def register_email2(request):
    return render (request,'register_email2.html')
def ClientPage(request):
    return render (request,'client.html')
def logout3(request):
    return render (request,'logout3.html')
def success(request):
    return render (request,'success.html')

def remainingAmt(request):
    return render (request,'remainingAmt.html')
#this is for remaining amount page
def savedata(request):
    if request.method=="POST":
        
        customername=request.POST.get('customername')
        email=request.POST.get('email')
        quotation=request.POST.get('quotation')
        advance=request.POST.get('advance')
        balance=request.POST.get('balance')
        en=remainingAmt(customername=customername,email=email,quotation=quotation,advance=advance,balance=balance)
        mydict={'customername':customername,'email':email,'quotation':quotation,'advance':advance,'balance':balance}
        en.save()
        r='data inserted'
        html_template='register_email2.html'
        html_message= render_to_string(html_template,context=mydict)
        
       

    return render (request,"payment.html",{'r':r})


 #this is for feedback  
def savemessage(request):
    if request.method=="POST":
        custname=request.POST.get('custname')
        
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        pn=feedback(custname=custname,email=email,phone=phone,message=message)
    
        pn.save()
        p='data inserted'
       
    return render (request,"feedback.html",{'p':p})
   
      

        # Handle other payment types
        
    # Render the initial form


def customer_details(request, customer_id):
    customerdata = get_object_or_404(customerdata, pk=customer_id)
    return render(request, 'customer_details.html', {'customerdata': customerdata}) # Path to your success template


class CustomerdataCreateView(CreateView):
       model = customerdata
       form_class = CustomerForm
       template_name = 'home.html'
       success_url = reverse_lazy('customerdata_success') # Redirect to home page or wherever you want

# Helper function to generate unique customer ID (you can replace it with your own logic)
def generate_unique_id():
    # Implement your logic to generate a unique ID here
    # For simplicity, let's generate a random ID for demonstration
    import uuid
    return str(uuid.uuid4().hex)[:4]  # Generate a 10-character ID


def process_payment(request):
    if request.method == 'POST':
        payment_type = request.POST.get('paymentType')
        if payment_type == 'card':
            card_number = request.POST.get('cardNumber')
            # Process card payment
            return redirect('logout3')
        elif payment_type == 'upi':
            upi_id = request.POST.get('upiId')
            # Process UPI payment
            return HttpResponse('logout3')
    # If method is not POST or payment type is not recognized
    return HttpResponse('Payment processing failed.')   


def payment_form(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Process the payment logic here
            # For example, save the payment information to the database
            form.save()
            # Redirect to a success page
            return redirect('logout3')
    

def payment_success_view(request):
    return render(request, 'payment_success.html')    

def select_option(request):
    if request.method == 'POST':
        customer_id=request.POST.get('customer_id')
        option=request.POST.get('option')
        customization=request.POST.get('customization')
        form=Decoration(customer_id=customer_id,option=option,customization=customization)
        form.save()
        return redirect('savepayment')  # Redirect to a success page
    else:
        return render(request, 'image_template.html')

def image_template(request):
    return render (request,'image_template.html')

def savepayment(request):
    if request.method == "POST":
        customer_id = request.POST.get('customer_id')
        amount = request.POST.get('amount')
        card_number = request.POST.get('card_number')
        expiration_date = request.POST.get('expiration_date')
        cvv = request.POST.get('cvv')
        utr = request.POST.get('utr')

        # Create a payment instance
        paym = payment(
            customer_id=customer_id,
            amount=amount,
            card_number=card_number,
            expiration_date=expiration_date,
            cvv=cvv,
            utr=utr
        )

        # Save the payment instance to the database
        paym.save()

        message = 'Data inserted'  # Adjust the message as needed
        return redirect('logout')
    else:
        form = PaymentForm()  # Instantiate the PaymentForm

    return render(request, "payment.html", {'form': form})

        
    
def process_advance_amount(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        quotation = request.POST.get('quotation')
        advance = request.POST.get('advance')
        balance = request.POST.get('balance')
        # Save the advance amount to the database or do other processing as needed
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Method not allowed'})