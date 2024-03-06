"""
URL configuration for event project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from accounts import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('feedback/',views.feedback,name='feedback'),
    path('saveenquiry/',views.saveenquiry,name='saveenquiry'),
    path('savemessage/',views.savemessage,name='savemessage'),
    path('gallery/',views.gallery,name='gallery'),
    path('about/',views.about,name='about'),
    path('logout/',views.logout,name='logout'),
    path('client/',views.ClientPage,name='client'),
    path('remainingAmt/',views.remainingAmt,name='remainingAmt'),
    path('savedata/',views.savedata,name='savedata'),
    path('register_email/',views.register_email,name='register_email'),
    path('savepayment/', views.savepayment, name='savepayment'),
    path('customer/', views.customer_details, name='customer_details'),
    path('success/', views.success, name='success'),
   
    path('process_payment/', views.process_payment, name='process_payment'),
    path('select-option/', views.select_option, name='select_option'),
    path('customerdata/<str:customer_id>/', views.customer_details, name='customer_details'),
    path('image_template/',views.image_template,name='image_template'),
    path('process_advance_amount/', views.process_advance_amount, name='process_advance_amount'),
]
