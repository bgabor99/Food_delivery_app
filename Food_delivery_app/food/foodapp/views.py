from contextlib import redirect_stdout
from datetime import datetime
from email import message
from email.mime import image
from turtle import settiltangle
from wsgiref.util import request_uri
from django.http import HttpResponse
from multiprocessing import context
import re
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import FoodModel, CustomModel, OrderModel, Logger
from django.contrib.auth.models import User
from django. views. decorators. csrf import csrf_exempt
import logging
import random
from django_globals import globals
from django.conf import settings
from .filters import FoodFilter, LogFilter


# Get an instance of loggers
logger = logging.getLogger(__name__)
db_logger = logging.getLogger('db')

#region functions for logging
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def getInfosForLog(request):
    infosDict = {
        'user' : request.user.username,
        'date' :  str(datetime.now()),
        'ipAddress' : str(get_client_ip(request)),
        'requestMethod' : str(request.method),
    }
    return infosDict


def createLog(logInfos, logMsg, viewFunctionCalled, priorityInt, priorityString):
    logDetails = logInfos['date'] + ' from ' + logInfos['ipAddress'] + ' with ' + logInfos['requestMethod'] + ' method'
    logger.warning(logMsg + logDetails)
    db_logger.warning(logMsg + logDetails)
    Logger(user=logInfos['user'], datetime = logInfos['date'], ipaddress = logInfos['ipAddress'], requestMethod = logInfos['requestMethod'], viewFunctionCalled = viewFunctionCalled, priorityInt = priorityInt, priorityString = priorityString, message=logMsg).save()
#endregion


#region Page views
@csrf_exempt
def adminloginview(request):
    logInfos = getInfosForLog(request)
    logMsg = logInfos['user'] + ' Admin login page (/admin/) was opened '
    createLog(logInfos, logMsg, 'adminloginview', 1, 'Info')
    return render(request, "foodapp/adminlogin.html")


@csrf_exempt
def authenticateadmin(request):
    logInfos = getInfosForLog(request)
    logMsg = logInfos['user'] + ' Admin page (/admin/homepage/) was opened '
    createLog(logInfos, logMsg, 'authenticateadmin', 1, 'Info')
    username = request.POST.get('username', 'Nothing')
    password = request.POST.get('password', 'Nothing')
    user = authenticate(username = username, password=password)
    request.session['is_admin_logged_in'] = True
    # not exists or not superuser or admin is not logged in
    if user is None or user.is_superuser == False or 'is_admin_logged_in' not in request.session:
        logMsg = logInfos['user'] + ' tried to login /admin/homepage/ but he is NOT superuser '
        createLog(logInfos, logMsg, 'authenticateadmin', 2, 'Warning')
        messages.add_message(request, messages.ERROR, "Invalid credentials!")
        return redirect('adminloginpage')

    # user exists
    if user is not None and user.username=="admin":
        login(request, user)
        logMsg = logInfos['user'] + ' Admin logged in '
        createLog(logInfos, logMsg, 'authenticateadmin', 1, 'Info')
        request.session['is_admin_logged_in'] = True
        return redirect('adminhomepage')
        
    # user doesn't exist
    if user is None:
        logMsg = logInfos['user'] + ' Somebody tried to login as Admin with INVALID credentials '
        createLog(logInfos, logMsg, 'authenticateadmin', 2, 'Warning')
        messages.add_message(request, messages.ERROR, "Invalid credentials!")
        del request.session['is_admin_logged_in']
        return redirect('adminloginpage')


@csrf_exempt
def adminhomepageview(request):
    logInfos = getInfosForLog(request)
    if 'is_admin_logged_in' not in request.session:
        logMsg = logInfos['user'] + ' Somebody tried to open adminhomepageview (admin/homepage/) by URL '
        createLog(logInfos, logMsg, 'adminhomepageview', 2, 'Warning')
        return redirect('adminloginpage')
    logMsg = logInfos['user'] + ' adminhomepageview (admin/homepage/) was opened '
    createLog(logInfos, logMsg, 'adminhomepageview', 1, 'Info')
    context = {'foods' : FoodModel.objects.all()}
    return render(request, "foodapp/adminhomepage.html", context)


@csrf_exempt
def logoutadmin(request):
    logInfos = getInfosForLog(request)
    logMsg = logInfos['user'] + ' was logged out '
    createLog(logInfos, logMsg, 'logoutadmin', 1, 'Info')
    logout(request)
    return redirect('adminloginpage')


@csrf_exempt
def addfood(request):
    # add food object into the database
    logInfos = getInfosForLog(request)
    name = request.POST.get('foodname', "NoFoodName")
    details = request.POST.get('fooddetails', "NoDetails")
    price = request.POST.get('foodprice', "NoFoodPrice")
    allergen = request.POST.get('foodallergen', "NoFoodAllergen")

    # if a food with this name already exists
    if FoodModel.objects.filter(name = name).exists():
        logMsg = logInfos['user'] + ' CAN NOT add food (because already exists) '
        createLog(logInfos, logMsg, 'addfood', 2, 'Warning')
        messages.add_message(request, messages.ERROR, "Food already exists!")
        return redirect('adminhomepage')

    # upload food picture
    if len(request.FILES) != 0:
        img = request.FILES.get('img')
    else:
        img = 'foodapp/static/img/no_image_available.jpg'
    FoodModel(name = name, details=details, price = price, allergens = allergen, image = img).save()
    logMsg = logInfos['user'] + 'Admin added a food with this name:{name} and price:{price} and allergens:{allergen} at '.format(name=name, price=price, allergen=allergen)
    messages.add_message(request, messages.SUCCESS, "Food successfully added!")
    createLog(logInfos, logMsg, 'addfood', 1, 'Info')
    return redirect('adminhomepage')


@csrf_exempt
def deletefood(request, foodapk):
    # delete food object from the database
    logInfos = getInfosForLog(request)
    logMsg = logInfos['user'] + ' deleted a food  '
    createLog(logInfos, logMsg, 'deletefood', 1, 'Info')
    FoodModel.objects.filter(id = foodapk).delete()
    messages.add_message(request, messages.SUCCESS, "Food successfully deleted!")
    return redirect('adminhomepage')


@csrf_exempt
def homepageview(request):
    logInfos = getInfosForLog(request)
    logMsg = logInfos['user'] + ' Costumer homepage was opened '
    createLog(logInfos, logMsg, 'homepageview', 1, 'Info')
    return render(request, "foodapp/homepage.html")


@csrf_exempt
def usersignuppage(request):
    logInfos = getInfosForLog(request)
    logMsg = logInfos['user'] + ' Costumer homepage was opened '
    createLog(logInfos, logMsg, 'usersignuppage', 1, 'Info')
    return render(request, "foodapp/usersignuppage.html")


@csrf_exempt
def signupuser(request):
    logInfos = getInfosForLog(request)
    logMsg = logInfos['user'] + ' Costumer signup page was opened '
    createLog(logInfos, logMsg, 'signupuser', 1, 'Info')
    username = request.POST.get('username', "NothingUsername")
    password = request.POST.get('password', "NothingPassword")
    confirmPassword = request.POST.get('confirmPassword', "NothingconfirmPassword")
    phoneno = request.POST.get('phoneno', "NothingPhoneno")
    # if username already exists
    if User.objects.filter(username = username).exists():
        logMsg = logInfos['user'] + ' CAN NOT sign up (because already exists) '
        createLog(logInfos, logMsg, 'signupuser', 2, 'Warning')
        messages.add_message(request, messages.ERROR, "User already exists!")
        return redirect('usersignuppage')

    # if password and confirmPassword doesn't match
    if str(password) != str(confirmPassword):
        logMsg = logInfos['user'] + ' CAN NOT sign up (because password and confirm password not match)'
        createLog(logInfos, logMsg, 'signupuser', 2, 'Warning')
        messages.add_message(request, messages.ERROR, "Password and confirm password not match!")
        return redirect('usersignuppage')

    # if username doesn't exists already
    # creating user
    User.objects.create_user(username = username, password = password).save()
    lastobject = len(User.objects.all())-1
    CustomModel(userid = User.objects.all()[lastobject].id, phoneno = phoneno).save()
    logMsg = logInfos['user'] + ' successfully signed up '
    createLog(logInfos, logMsg, 'signupuser', 1, 'Info')
    messages.add_message(request, messages.SUCCESS, "User succesfully created!")
    return redirect('usersignuppage') 


@csrf_exempt
def userloginview(request):
    logInfos = getInfosForLog(request)
    logMsg = logInfos['user'] + ' Costumer login page was opened '
    createLog(logInfos, logMsg, 'userloginview', 1, 'Info')
    num = random.randint(1000, 9999)
    str_num = str(num)
    request.session['captcha_str'] = str_num
    context = {"captcha" : str_num}
    return render(request, "foodapp/userlogin.html", context)


@csrf_exempt
def userauthenticate(request):
    logInfos = getInfosForLog(request)
    logMsg = logInfos['user'] + ' Costumer tried to authenticate '
    createLog(logInfos, logMsg, 'userauthenticate', 1, 'Info')
    username = request.POST['username']
    password = request.POST['password']
    captcha = request.POST['captcha']
    if request.session['captcha_str'] != captcha or 'captcha_str' not in request.session:
        # TODO logging
        messages.add_message(request, messages.ERROR, "Invalid captcha!")
        return redirect('userloginpage')
        
    user = authenticate(username = username, password = password)
    # user exists
    if user is not None:
        logMsg = logInfos['user'] + ' successfully to authenticated  '
        createLog(logInfos, logMsg, 'userauthenticate', 1, 'Info')
        login(request, user)
        return redirect('customerpage')

    #user doesn't exist
    if user is None:
        logMsg = logInfos['user'] + ' was NOT authenticated (because this user does not exists yet in the database)  '
        createLog(logInfos, logMsg, 'userauthenticate', 2, 'Warning')
        messages.add_message(request, messages.ERROR, "Invalid credentials!")
        return redirect('userloginpage')


@csrf_exempt
def customerwelcomeview(request):
    logInfos = getInfosForLog(request)
    if request.user.is_authenticated == False:
        logMsg = logInfos['user'] + 'Somebody tried to reach directly /costumer/welcome/ page by URL  '
        createLog(logInfos, logMsg, 'customerwelcomeview', 2, 'Warning')
        return redirect('userloginpage')

    username = request.user.username
    logMsg = logInfos['user'] + ' welcome page was opened  '
    createLog(logInfos, logMsg, 'customerwelcomeview', 1, 'Info')
    foods = FoodModel.objects.all()
    myFilter = FoodFilter(request.GET, queryset=foods)
    foods =  myFilter.qs

    context = {'username' : username,  'foods' : foods, 'filter': myFilter}
    return render(request, "foodapp/customerwelcome.html", context)


@csrf_exempt
def userlogout(request):
    username = request.user.username
    logInfos = getInfosForLog(request)
    logMsg = logInfos['user'] + ' logged out  '
    createLog(logInfos, logMsg, 'userlogout', 1, 'Info')
    logout(request)
    return redirect('userloginpage') 


@csrf_exempt
def placeorder(request):
    logInfos = getInfosForLog(request)
    if request.user.is_authenticated == False:
        logMsg = logInfos['user'] + ' Somebody tried to reach directly /placeorder/ page by URL  '
        createLog(logInfos, logMsg, 'placeorder', 2, 'Warning')
        return redirect('userloginpage')
    username = request.user.username # logged in user
    phoneno = CustomModel.objects.filter(userid = request.user.id).first().phoneno
    # delivery informations
    city = request.POST.get('city', "NothingCity")
    address = request.POST.get('address', "NothingAddress")
    zip = request.POST.get('zip', 0)
    # billing informations
    billingCity = request.POST.get('billingCity', "NothingBillingCity")
    billingAddress = request.POST.get('billingAddress', "NothingBillingAddress")
    billingZip = request.POST.get('billingZip', 0)

    orderitems=""
    totalPrice = 0
    foodsWithQuantitydict = {}
    for food in FoodModel.objects.all():
        foodid = food.id
        name = food.name
        priceForOne = food.price
        quantity = request.POST.get(str(foodid), "nothing")


        if str(quantity)!="0" and quantity!="nothing" and quantity!="":
            price = int(quantity)*int(priceForOne)
            orderitems = orderitems + name + ', price: ' + str(priceForOne) + ', quantity: ' + quantity + ';'
            totalPrice = totalPrice + price
            foodsWithQuantitydict.update({name : int(quantity)})

    if totalPrice == 0:
        logMsg = logInfos['user'] + ' placed an order with 0 quantity '
        createLog(logInfos, logMsg, 'placeorder', 2, 'warning')
        messages.add_message(request, messages.ERROR, "You have to order minimum 1 quantity!")
        return redirect('../costumer/welcome/')

    totalPriceStr = str(totalPrice)
    fullAddress = str(zip) + " " + str(city) + ", " + str(address)
    if billingCity=="" or billingAddress=="" or billingZip=="":
        fullBillingAddress = fullAddress
    elif billingCity=="NothingBillingCity" or billingAddress=="NothingBillingAddress" or billingZip==0:
        fullBillingAddress = fullAddress
    else:
        fullBillingAddress = str(billingZip) + " " + str(billingCity) + ", " + str(billingAddress)

    # save into Order database
    order = OrderModel(username = username, phoneno = phoneno, address = fullAddress, billingAddress = fullBillingAddress, orderitems = orderitems, total=totalPriceStr, status='pending')
    order.save()

    # update orderedCount for every ordered food
    for foodName in foodsWithQuantitydict:
        foodModel = FoodModel.objects.filter(name = foodName)
        orderCount = foodModel.first().orderedCount
        foodModel.update(orderedCount = orderCount + foodsWithQuantitydict[foodName])

    logMsg = logInfos['user'] + ' placed an order '
    createLog(logInfos, logMsg, 'placeorder', 1, 'Info')
    messages.add_message(request, messages.SUCCESS, "Order placed, thank you for your order!")
    return redirect('../costumer/welcome/')


@csrf_exempt
def userorders(request):
    logInfos = getInfosForLog(request)
    if request.user.is_authenticated == False:
        logMsg = logInfos['user'] + 'Somebody tried to reach directly /userorders/ page by URL  '
        createLog(logInfos, logMsg, 'userorders', 2, 'Warning')
        return redirect('userloginpage')
    logMsg = logInfos['user'] + ' viewed his orders '
    createLog(logInfos, logMsg, 'userorders', 1, 'Info')
    user = request.user.username
    orders = OrderModel.objects.filter(username = user)
    context = {'orders' : orders}
    return render(request, 'foodapp/userorders.html', context)


@csrf_exempt
def adminorders(request):
    logInfos = getInfosForLog(request)
    if 'is_admin_logged_in' not in request.session:
        logMsg = logInfos['user'] + ' Somebody tried to open admin orders page (admin/logs/) by URL '
        createLog(logInfos, logMsg, 'adminorders', 2, 'Warning')
        return redirect('adminloginpage')
    logMsg = logInfos['user'] + ' viewed all orders '
    createLog(logInfos, logMsg, 'adminorders', 1, 'Info')
    orders = OrderModel.objects.all()
    context = {'orders' : orders}
    return render(request, 'foodapp/adminorders.html', context)


@csrf_exempt
def acceptorder(request, orderpk):
    logInfos = getInfosForLog(request)
    logMsg = logInfos['user'] + ' accepted an order '
    createLog(logInfos, logMsg, 'acceptorder', 1, 'Info')
    order = OrderModel.objects.filter(id = orderpk).first()
    order.status = "accepted"
    order.save()
    return redirect(request.META['HTTP_REFERER'])


@csrf_exempt
def declineorder(request, orderpk):
    logInfos = getInfosForLog(request)
    logMsg = logInfos['user'] + '  declined an order '
    createLog(logInfos, logMsg, 'declineorder', 1, 'Info')
    order = OrderModel.objects.filter(id = orderpk).first()
    order.status = "declined"
    order.save()
    return redirect(request.META['HTTP_REFERER'])


@csrf_exempt
def deliveredorder(request, orderpk):
    logInfos = getInfosForLog(request)
    logMsg = logInfos['user'] + ' changed status to delivered in an order '
    createLog(logInfos, logMsg, 'deliveredorder', 1, 'Info')
    order = OrderModel.objects.filter(id = orderpk).first()
    order.status = "delivered"
    order.save()
    return redirect(request.META['HTTP_REFERER']) 


@csrf_exempt
def rateaction(request, orderpk):
    logInfos = getInfosForLog(request)
    logMsg = logInfos['user'] + ' rated an order '
    createLog(logInfos, logMsg, 'rateaction', 1, 'Info')
    if OrderModel.objects.filter(id = orderpk).first() is not None:
        order = OrderModel.objects.filter(id = orderpk).first()
        # saving rate in orderModel
        rateValue = request.POST.get("rateSelect", "Nothing")
        order.rate = rateValue
        order.save()

        # increase user givenRatesCounter and givenRatesSum in users costumModel
        username = order.username
        if User.objects.filter(username = username).first() != None:
            auth_user_id = User.objects.filter(username = username).first().id
            if username != "" and auth_user_id != "":
                if CustomModel.objects.filter(userid = auth_user_id).first() != None:
                    costumer = CustomModel.objects.filter(userid = auth_user_id)
                    costumerPrevgivenRatesCounter = costumer.first().givenRatesCounter
                    costumerPrevgivenRatesSumn = costumer.first().givenRatesSum
                    costumer.update(givenRatesCounter = costumerPrevgivenRatesCounter + 1)
                    costumer.update(givenRatesSum = costumerPrevgivenRatesSumn + int(rateValue))

        # increase food ratesCounter and and ratesSum in foodModel
        ratedfoodNamesList = order.ratedFoodNamesFromOrderitemsList()
        for ratedFoodName in ratedfoodNamesList:
            if FoodModel.objects.filter(name = ratedFoodName).first() != None:
                food = FoodModel.objects.filter(name = ratedFoodName)
                foodPrevRatesSum = food.first().ratesSum
                foodPrevRatesCounter = food.first().ratesCounter
                food.update(ratesSum = foodPrevRatesSum + int(order.rate), ratesCounter = foodPrevRatesCounter + 1)

    return redirect(request.META['HTTP_REFERER'])


@csrf_exempt
def usermanage(request):
    logInfos = getInfosForLog(request)
    if 'is_admin_logged_in' not in request.session:
        logMsg = logInfos['user'] + ' Somebody tried to open usemanage page (admin/logs/) by URL '
        createLog(logInfos, logMsg, 'usermanage', 2, 'Warning')
        return redirect('adminloginpage')
    logMsg = logInfos['user'] + ' viewed all users '
    createLog(logInfos, logMsg, 'usermanage', 1, 'Info')
    users = CustomModel.objects.all()
    auth_users = User.objects.all()
    context = {'users' : users, 'auth_users' : auth_users}
    return render(request, 'foodapp/usermanage.html', context)


@csrf_exempt
def deleteuser(request, userid, username):
    logInfos = getInfosForLog(request)
    logMsg = logInfos['user'] + ' deleted a user '
    createLog(logInfos, logMsg, 'deleteuser', 1, 'Info')
    CustomModel.objects.filter(userid = userid).delete()
    User.objects.filter(id = userid).delete()
    OrderModel.objects.filter(username = username).delete()
    return redirect('usermanage')


@csrf_exempt
def deleteorder(request, orderpk):
    logInfos = getInfosForLog(request)
    logMsg = logInfos['user'] + ' deleted an order '
    createLog(logInfos, logMsg, 'deleteorder', 1, 'Info')
    OrderModel.objects.filter(id = orderpk).delete()
    return redirect('adminorders')


@csrf_exempt
def adminlogs(request):
    logInfos = getInfosForLog(request)
    if 'is_admin_logged_in' not in request.session:
        logMsg = logInfos['user'] + ' Somebody tried to open adminlog page (admin/logs/) by URL '
        createLog(logInfos, logMsg, 'adminlogs', 2, 'Warning')
        return redirect('adminloginpage')
    logMsg = logInfos['user'] + ' admin logs (admin/logs/) was opened '
    createLog(logInfos, logMsg, 'adminlogs', 1, 'Info')
    logs = Logger.objects.all()
    logFilter = LogFilter(request.GET, queryset=logs)
    logs =  logFilter.qs
    context = {'logs' : logs, 'filter': logFilter}
    return render(request, "foodapp/adminlogs.html", context)


@csrf_exempt
def deletelog(request, logid):
    logInfos = getInfosForLog(request)
    logMsg = logInfos['user'] + ' deleted a log '
    createLog(logInfos, logMsg, 'deletelog', 1, 'Info')
    Logger.objects.filter(id = logid).delete()
    return redirect('adminlogs')


@csrf_exempt
def deletealloflogs(request):
    logInfos = getInfosForLog(request)
    logMsg = logInfos['user'] + ' deleted a all logs '
    createLog(logInfos, logMsg, 'deletealloflogs', 1, 'Info')
    Logger.objects.all().delete()
    return redirect('adminlogs')


@csrf_exempt
def userprofile(request):
    logInfos = getInfosForLog(request)
    if request.user.is_authenticated == False:
        logMsg = logInfos['user'] + 'Somebody tried to reach directly /userprofile/ page by URL  '
        createLog(logInfos, logMsg, 'userprofile', 2, 'Warning')
        return redirect('userloginpage')
    logMsg = logInfos['user'] + ' viewed his profile '
    createLog(logInfos, logMsg, 'userorprofile', 1, 'Info')
    userName = logInfos['user']
    users = CustomModel.objects.all()
    auth_user = User.objects.filter(username = userName)
    context = {'users' : users, 'auth_users' : auth_user}
    return render(request, 'foodapp/userprofile.html', context)


@csrf_exempt
def deleteuserrequest(request, userid):
    logInfos = getInfosForLog(request)
    logMsg = logInfos['user'] + ' viewed his profile '
    createLog(logInfos, logMsg, 'deleteuserrequest', 1, 'Info')
    user = CustomModel.objects.filter(userid = userid).first()
    user.requestToBeDeleted = True
    user.save()
    return redirect(request.META['HTTP_REFERER'])


@csrf_exempt
def contactandsupportpage(request):
    logInfos = getInfosForLog(request)
    logMsg = logInfos['user'] + ' Costumer contactandsupportpage was opened '
    createLog(logInfos, logMsg, 'contactandsupportpage', 1, 'Info')
    return render(request, "foodapp/contactandsupportpage.html")


@csrf_exempt
def cartepage(request):
    logInfos = getInfosForLog(request)
    logMsg = logInfos['user'] + ' Costumer cartepage was opened '
    createLog(logInfos, logMsg, 'cartepage', 1, 'Info')
    foods = FoodModel.objects.all()
    context = {'foods' : foods}
    return render(request, "foodapp/cartepage.html", context)


@csrf_exempt
def updateFoodByName(foodName, foodNewName, foodNewDetails, foodNewPrice, foodNewAllergen):
    if FoodModel.objects.filter(name = foodName).first() is None:
        return
    if foodNewDetails != "":
        FoodModel.objects.filter(name = foodName).update(details=foodNewDetails)
    if foodNewPrice != "":
        FoodModel.objects.filter(name = foodName).update(price=foodNewPrice)
    if foodNewAllergen != "":
        FoodModel.objects.filter(name = foodName).update(allergens=foodNewAllergen)
    # has to be the last, because update works by foods name
    if foodNewName != "":
        FoodModel.objects.filter(name = foodName).update(name=foodNewName)


@csrf_exempt
def modifyfood(request):
    # modify food object in the database by its name
    logInfos = getInfosForLog(request)
    foodNameValue = request.POST.get('foodModifyName', "NoFoodName")
    foodNewName = request.POST.get('foodname', "NoFoodName")
    foodNewDetails = request.POST.get('fooddetails', "NoDetails")
    foodNewPrice = request.POST.get('foodprice', "NoFoodPrice")
    foodNewAllergen = request.POST.get('foodallergen', "NoFoodAllergen")
    
    # if foodname already exists in the database
    if FoodModel.objects.filter(name = foodNewName).exists():
        logMsg = logInfos['user'] + ' CAN NOT modify food (because already exists) '
        createLog(logInfos, logMsg, 'modifyfood', 2, 'Warning')
        messages.add_message(request, messages.ERROR, "Food already exists!")
        return redirect('adminhomepage')

    if FoodModel.objects.filter(name = foodNameValue).first() is None or foodNameValue == "NoFoodName":
        logMsg = logInfos['user'] + ' NOT modified a food (because this food id does not exists yet in the database)  '
        createLog(logInfos, logMsg, 'modifyfood', 2, 'Warning')
        messages.add_message(request, messages.ERROR, "Invalid food id!")
        return redirect('adminhomepage')

    if(foodNewName=="NoFoodName" and foodNewDetails=="NoDetails" and foodNewPrice=="NoFoodPrice" and foodNewAllergen=="NoFoodAllergen"):
        logMsg = logInfos['user'] + ' NOT modified a food (because no modify data input added)  '
        createLog(logInfos, logMsg, 'modifyfood', 2, 'Warning')
        messages.add_message(request, messages.ERROR, "No modify inputs!")
        return redirect('adminhomepage')

    if(foodNewName=="" and foodNewDetails=="" and foodNewPrice=="" and foodNewAllergen==""):
        logMsg = logInfos['user'] + ' NOT modified a food (because no modify data input added)  '
        createLog(logInfos, logMsg, 'modifyfood', 2, 'Warning')
        messages.add_message(request, messages.ERROR, "No modify inputs!")
        return redirect('adminhomepage')


    updateFoodByName(foodNameValue, foodNewName, foodNewDetails, foodNewPrice, foodNewAllergen)
    logMsg = logInfos['user'] + 'Admin modified a food with this name:{name} and price:{price} and allergens:{allergen} at '.format(name=foodNewName, price=foodNewPrice, allergen=foodNewAllergen)
    createLog(logInfos, logMsg, 'modifyfood', 1, 'Info')
    messages.add_message(request, messages.SUCCESS, "Food successfully modified!")
    return redirect('adminhomepage')


@csrf_exempt
def zerofoodordercounters(request):
    logInfos = getInfosForLog(request)
    logMsg = logInfos['user'] + ' restarted order counters '
    createLog(logInfos, logMsg, 'zerofoodordercounters', 1, 'Info')
    FoodModel.objects.all().update(orderedCount = 0)
    return redirect('adminhomepage')


@csrf_exempt
def zerofoodratecounters(request):
    logInfos = getInfosForLog(request)
    logMsg = logInfos['user'] + ' restarted rate counters '
    createLog(logInfos, logMsg, 'zerofoodratecounters', 1, 'Info')
    FoodModel.objects.all().update(ratesSum = 0, ratesCounter = 0)
    return redirect('adminhomepage')
#endregion