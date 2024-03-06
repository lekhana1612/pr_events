from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from accounts import views
from .views import process_payment
from .views import savepayment
from .views import customer_details
from .views import CustomerdataCreateView, CustomerdataSuccessView
from .views import select_option
from django.conf.urls.static import static

from.views import savemessage
from.views import process_advance_amount

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('feedback/',views.feedback,name='feedback'),
    path('savemessage/',views.savemessage,name='savemessage'),
    path('gallery/',views.gallery,name='gallery'),
    path('about/',views.about,name='about'),
    path('logout/',views.logout,name='logout'),
    path('client/',views.ClientPage,name='client'),
   
    path('savedata/',views.savedata,name='savedata'),
    path('register_email/',views.register_email,name='register_email'),
    path('register_email2/',views.register_email2,name='register_email2'),
    path('customer/', customer_details, name='customer_details'),
    path('saveenquiry/',views.saveenquiry,name='saveenquiry'),
    path('customerdataa/', CustomerdataCreateView.as_view(), name='customerdata_create'),
    path('successnn/', CustomerdataSuccessView.as_view(), name='customerdata_success'),
    path('success/',views.success,name='logout'),
    path('savepayment/', views.savepayment, name='savepayment'),
    
    path('select-option/', select_option, name='select_option'),
    path('customerdata/<str:customer_id>/', views.customer_details, name='customer_details'),
    path('process_advance_amount/', views.process_advance_amount, name='process_advance_amount'),
]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)