from unicodedata import name
from django.contrib import admin
from django.urls import path
from .views import adminloginview, authenticateadmin, adminhomepageview, logoutadmin,  addfood, deletefood
from .views import homepageview, signupuser, userloginview, customerwelcomeview, userauthenticate, userlogout, placeorder
from .views import userorders, adminorders, acceptorder, declineorder, deliveredorder, rateaction
from .views import usermanage, deleteuser, deleteorder, adminlogs, deletelog, deletealloflogs, userprofile, deleteuserrequest
from .views import usersignuppage, contactandsupportpage, cartepage, modifyfood, zerofoodordercounters, zerofoodratecounters

urlpatterns = [
    path('admin/', adminloginview, name='adminloginpage'),
    path('adminauthenticate/', authenticateadmin, name='adminauthenticate'),
    path('admin/homepage/', adminhomepageview, name='adminhomepage'),
    path('adminlogout/', logoutadmin, name='adminlogout'),
    path('addfood/', addfood, name='addfood'),
    path('deletefood/<int:foodapk>/', deletefood, name='deletefood'),
    path('', homepageview, name='homepage'),
    path('signupuser/', signupuser, name='signupuser'),
    path('loginuser/', userloginview, name='userloginpage'),
    path('costumer/welcome/', customerwelcomeview, name='customerpage'),
    path('costumer/authenticate/', userauthenticate, name='userauthenticate'),
    path('userlogout/', userlogout, name='userlogout'),
    path('placeorder/', placeorder, name='placeorder'),
    path('userorders/', userorders, name='userorders'),
    path('userorders/', userorders, name='userorders'),
    path('adminorders/', adminorders, name='adminorders'),
    path('acceptorder/<int:orderpk>/', acceptorder, name='acceptorder'),
    path('declineorder/<int:orderpk>/', declineorder, name='declineorder'),
    path('deliveredorder/<int:orderpk>/', deliveredorder, name='deliveredorder'),
    path('rateaction/<int:orderpk>/', rateaction, name='rateaction'),
    path('usermanage/', usermanage, name='usermanage'),
    path('deleteuser/<int:userid>/<slug:username>/', deleteuser, name='deleteuser'),
    path('deleteorder/<int:orderpk>/', deleteorder, name='deleteorder'),
    path('adminlogs/', adminlogs, name='adminlogs'),
    path('deletelog/<int:logid>/', deletelog, name='deletelog'),
    path('deletealloflogs/', deletealloflogs, name='deletealloflogs'),
    path('userprofile/', userprofile, name='userprofile'),
    path('deleteuserrequest/<int:userid>/', deleteuserrequest, name='deleteuserrequest'),
    path('usersignuppage/', usersignuppage, name='usersignuppage'),
    path('contact/', contactandsupportpage, name='supportpage'),
    path('support/', contactandsupportpage, name='contactpage'),
    path('carte/', cartepage, name='carte'),
    path('modifyfood/', modifyfood, name='modifyfood'),
    path('zerofoodordercounters/', zerofoodordercounters, name='zerofoodordercounters'),
    path('zerofoodratecounters/', zerofoodratecounters, name='zerofoodratecounters'),
]
