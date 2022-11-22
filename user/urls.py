from django.urls import path
from user import views

urlpatterns = [
    path('', views.myhome, name='home'),
    path('menus/', views.menus, name='menus'),
    path('contactus/', views.contactus, name='contactus'),
    
    path('quatation/', views.quatation,name='qatation'),
    path('ourservices/', views.ourservices, name='ourservices'),
   #path('ourservices/', views.ourservices),
    path('gallary/', views.gallary, name='gallary'),
    path('termsandconditions/', views.termsandconditions, name='termsandconditions'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('customerinfo/', views.mycustomer ,name='customerinfo'),
    path('packagesilver/', views.packagesilver, name='packagesilver'),
    path('packagegold/', views.packagegold, name='packagegold'),
    path('packageplatinum/', views.packageplatinum, name='packageplatinum'),
   # path('newcustomer/', views.newcustomer,name='newRecord'),

]
