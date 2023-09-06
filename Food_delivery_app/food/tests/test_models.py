from datetime import datetime
from django.test import TestCase
from foodapp.models import FoodModel, CustomModel, OrderModel, Logger
from django.core.files import File


class TestModels(TestCase):

    def setUp(self):
        #region Food_creations
        # every attributes added
        self.food1_every_attributes = FoodModel.objects.create(
            name='Name1',
            details='Details1',
            price=1,
            allergens='Allergens1',
            image = File(file=b""),
            orderedCount = 1,
            ratesSum = 1,
            ratesCounter = 1,
        )

        # no details
        self.food2_no_details = FoodModel.objects.create(
            name='Name2',
            price=2,
            allergens='Allergens2',
            image = File(file=b""),
            orderedCount = 2,
            ratesSum = 2,
            ratesCounter = 2,
        )

        # no name
        self.food3_no_name = FoodModel.objects.create(
            details='Details3',
            price=3,
            allergens='Allergens3',
            image = File(file=b""),
            orderedCount = 3,
            ratesSum = 3,
            ratesCounter = 3,
        )

        # no price
        self.food4_no_price = FoodModel.objects.create(
            name='Name4',
            details='Details4',
            allergens='Allergens4',
            image = File(file=b""),
            orderedCount = 4,
            ratesSum = 4,
            ratesCounter = 4,
        )

        # no allergens
        self.food5_no_allergens = FoodModel.objects.create(
            name='Name5',
            details='Details5',
            price=5,
            image = File(file=b""),
            orderedCount = 5,
            ratesSum = 5,
            ratesCounter = 5,
        )

        # no image
        self.food6_no_image = FoodModel.objects.create(
            name='Name6',
            details='Details6',
            price=6,
            allergens='Allergens6',
            orderedCount = 6,
            ratesSum = 6,
            ratesCounter = 6,
        )

        # no orderedCount
        self.food7_no_orderedCount = FoodModel.objects.create(
            name='Name7',
            details='Details7',
            price=7,
            allergens='Allergens7',
            ratesSum = 7,
            ratesCounter = 7,
        )

        # no ratesSum
        self.food8_no_ratesSum = FoodModel.objects.create(
            name='Name8',
            details='Details8',
            price=8,
            allergens='Allergens8',
            orderedCount = 9,
            ratesCounter = 8,
        )

        # no ratesCounter
        self.food9_no_ratesCounter = FoodModel.objects.create(
            name='Name9',
            details='Details9',
            price=9,
            allergens='Allergens9',
            orderedCount = 9,
            ratesSum = 9,
        )
        #endregion


        #region CustomModel_creations
        # every attributes added
        self.customer1_every_attributes = CustomModel.objects.create(
            userid=1,
            phoneno='1',
            requestToBeDeleted=True,
            givenRatesCounter=1,
            givenRatesSum=1,
        )

        # no userid
        self.customer2_no_userid = CustomModel.objects.create(
            phoneno='2',
            requestToBeDeleted=True,
            givenRatesCounter=2,
            givenRatesSum=2,
        )

        # no phoneno
        self.customer3_no_phoneno = CustomModel.objects.create(
            userid=3,
            requestToBeDeleted=True,
            givenRatesCounter=3,
            givenRatesSum=3,
        )

        # no requestToBeDeleted
        self.customer4_no_requestToBeDeleted = CustomModel.objects.create(
            userid=4,
            phoneno='4',
            givenRatesCounter=4,
            givenRatesSum=4,
        )

        # no givenRatesCounter
        self.customer5_no_givenRatesCounter = CustomModel.objects.create(
            userid=5,
            phoneno='5',
            givenRatesSum=5,
        )

        # no givenRatesSum
        self.customer6_no_givenRatesSum = CustomModel.objects.create(
            userid=6,
            phoneno='6',
            givenRatesCounter=6,
        )
        #endregion

        #region OrderModel_creations
        # every attributes added
        self.order0_ratedFoodNamesFromOrderitemsList_1_foods = OrderModel.objects.create(
            username='UserName0',
            phoneno='0',
            address='Address0',
            billingAddress='billingAddress0',
            orderitems='Food1 burger, price: 2500, quantity: 2;',
            total='Total0',
            status='Status0',
            rate='Rate0',
        )

        self.order0_ratedFoodNamesFromOrderitemsList_2_foods = OrderModel.objects.create(
            username='UserName0',
            phoneno='0',
            address='Address0',
            billingAddress='billingAddress0',
            orderitems='Food1 burger, price: 2500, quantity: 2;Food2 pizza, price: 1500, quantity: 1;',
            total='Total0',
            status='Status0',
            rate='Rate0',
        )

        self.order0_ratedFoodNamesFromOrderitemsList_3_foods = OrderModel.objects.create(
            username='UserName0',
            phoneno='0',
            address='Address0',
            billingAddress='billingAddress0',
            orderitems='Food1 burger, price: 2500, quantity: 2;Food2 pizza, price: 1500, quantity: 1;Food3 pizza burger, price: 5000, quantity: 1;',
            total='Total0',
            status='Status0',
            rate='Rate0',
        )

        self.order1_every_attributes = OrderModel.objects.create(
            username='UserName1',
            phoneno='1',
            address='Address1',
            billingAddress='billingAddress1',
            orderitems='OrderItems1',
            total='Total1',
            status='Status1',
            rate='Rate1',
        )

        # no username
        self.order2_no_username = OrderModel.objects.create(
            phoneno='2',
            address='Address2',
            billingAddress='billingAddress2',
            orderitems='OrderItems2',
            total='Total2',
            status='Status2',
            rate='Rate2',
        )

        # no phoneno
        self.order3_no_phoneno = OrderModel.objects.create(
            username='UserName3',
            address='Address3',
            billingAddress='billingAddress3',
            orderitems='OrderItems3',
            total='Total3',
            status='Status3',
            rate='Rate3',
        )

        # no address
        self.order4_no_address = OrderModel.objects.create(
            username='UserName4',
            phoneno='4',
            billingAddress='billingAddress4',
            orderitems='OrderItems4',
            total='Total4',
            status='Status4',
            rate='Rate4'
        )

        # no orderitems
        self.order5_no_orderitems = OrderModel.objects.create(
            username='UserName5',
            phoneno='5',
            address='Address5',
            billingAddress='billingAddress5',
            total='Total5',
            status='Status5',
            rate='Rate5',
        )

        # no total
        self.order6_no_total = OrderModel.objects.create(
            username='UserName6',
            phoneno='6',
            address='Address6',
            billingAddress='billingAddress6',
            orderitems='OrderItems6',
            status='Status6',
            rate='Rate6',
        )

        # no status
        self.order7_no_status = OrderModel.objects.create(
            username='UserName7',
            phoneno='7',
            address='Address7',
            billingAddress='billingAddress7',
            orderitems='OrderItems7',
            total='Total7',
            rate='Rate7',
        )

        # no rate
        self.order8_no_rate = OrderModel.objects.create(
            username='UserName8',
            phoneno='8',
            address='Address8',
            billingAddress='billingAddress8',
            orderitems='OrderItems8',
            total='Total8',
            status='Status8',
        )

        # no billingAddress
        self.order9_no_billingAddress = OrderModel.objects.create(
            username='UserName9',
            phoneno='9',
            address='Address9',
            orderitems='OrderItems9',
            total='Total9',
            status='Status9',
            rate='Rate9',
        )
        #endregion

        #region Logger_creations
        # every attributes added
        self.logger1_every_attributes = Logger.objects.create(
            user='user1',
            datetime='datetime1',
            ipaddress='ipaddress1',
            requestMethod='requestMethod1',
            viewFunctionCalled='viewFunctionCalled1',
            priorityInt=1,
            priorityString='priorityString1',
            message='message1',
        )

        # no user
        self.logger2_no_user = Logger.objects.create(
            datetime='datetime2',
            ipaddress='ipaddress2',
            requestMethod='requestMethod2',
            viewFunctionCalled='viewFunctionCalled2',
            priorityInt=2,
            priorityString='priorityString2',
            message='message2',
        )

        # no datetime
        self.logger3_no_datetime = Logger.objects.create(
            user='user3',
            ipaddress='ipaddress3',
            requestMethod='requestMethod3',
            viewFunctionCalled='viewFunctionCalled3',
            priorityInt=3,
            priorityString='priorityString3',
            message='message3',
        )

        # no ipaddress
        self.logger4_no_ipaddress = Logger.objects.create(
            user='user4',
            datetime='datetime4',
            requestMethod='requestMethod4',
            viewFunctionCalled='viewFunctionCalled4',
            priorityInt=4,
            priorityString='priorityString4',
            message='message4',
        )

        # no requestMethod
        self.logger5_no_requestMethod = Logger.objects.create(
            user='user5',
            datetime='datetime5',
            ipaddress='ipaddress5',
            viewFunctionCalled='viewFunctionCalled5',
            priorityInt=5,
            priorityString='priorityString5',
            message='message5',
        )

        # no viewFunctionCalled
        self.logger6_no_viewFunctionCalled = Logger.objects.create(
            user='user6',
            datetime='datetime6',
            ipaddress='ipaddress6',
            requestMethod='requestMethod6',
            priorityInt=6,
            priorityString='priorityString6',
            message='message6',
        )

        # no priorityInt
        self.logger7_no_priorityInt = Logger.objects.create(
            user='user7',
            datetime='datetime7',
            ipaddress='ipaddress7',
            requestMethod='requestMethod7',
            viewFunctionCalled='viewFunctionCalled7',
            priorityString='priorityString7',
            message='message7',
        )

        # no priorityString
        self.logger8_no_priorityString = Logger.objects.create(
            user='user8',
            datetime='datetime8',
            ipaddress='ipaddress8',
            requestMethod='requestMethod8',
            viewFunctionCalled='viewFunctionCalled8',
            priorityInt=8,
            message='message8',
        )

        # no message
        self.logger9_no_message = Logger.objects.create(
            user='user9',
            datetime='datetime9',
            ipaddress='ipaddress9',
            requestMethod='requestMethod9',
            viewFunctionCalled='viewFunctionCalled9',
            priorityInt=9,
            priorityString='priorityString9',
        )
        #endregion

    #region FoodModel_tests
    def test_FoodModel_object_creation_every_attributes(self):
        food = self.food1_every_attributes
        self.assertEqual(food.name, 'Name1')
        self.assertEqual(food.price, 1)
        self.assertEqual(food.allergens, 'Allergens1')
        self.assertIsNotNone(food.image)
        self.assertEqual(food.orderedCount, 1)
        self.assertEqual(food.ratesSum, 1)
        self.assertEqual(food.ratesCounter, 1)


    def test_FoodModel_object_creation_details_default(self):
        food = self.food2_no_details
        self.assertEqual(food.name, 'Name2')
        self.assertEqual(food.details, 'NoDetails')
        self.assertEqual(food.price, 2)
        self.assertEqual(food.allergens, 'Allergens2')
        self.assertIsNotNone(food.image)
        self.assertEqual(food.orderedCount, 2)
        self.assertEqual(food.ratesSum, 2)
        self.assertEqual(food.ratesCounter, 2)
        


    def test_FoodModel_object_creation_name_default(self):
        food = self.food3_no_name
        self.assertEqual(food.name, 'No name')
        self.assertEqual(food.details, 'Details3')
        self.assertEqual(food.price, 3)
        self.assertEqual(food.allergens, 'Allergens3')
        self.assertIsNotNone(food.image)
        self.assertEqual(food.orderedCount, 3)
        self.assertEqual(food.ratesSum, 3)
        self.assertEqual(food.ratesCounter, 3)


    def test_FoodModel_object_creation_price_default(self):
        food = self.food4_no_price
        self.assertEqual(food.name, 'Name4')
        self.assertEqual(food.details, 'Details4')
        self.assertEqual(food.price, 0)
        self.assertEqual(food.allergens, 'Allergens4')
        self.assertIsNotNone(food.image)
        self.assertEqual(food.orderedCount, 4)
        self.assertEqual(food.ratesSum, 4)
        self.assertEqual(food.ratesCounter, 4)


    def test_FoodModel_object_creation_allergens_default(self):
        food = self.food5_no_allergens
        self.assertEqual(food.name, 'Name5')
        self.assertEqual(food.details, 'Details5')
        self.assertEqual(food.price, 5)
        self.assertEqual(food.allergens, 'No allergens')
        self.assertIsNotNone(food.image)
        self.assertEqual(food.orderedCount, 5)
        self.assertEqual(food.ratesSum, 5)
        self.assertEqual(food.ratesCounter, 5)


    def test_FoodModel_object_creation_image_default(self):
        food = self.food6_no_image
        self.assertEqual(food.name, 'Name6')
        self.assertEqual(food.details, 'Details6')
        self.assertEqual(food.price, 6)
        self.assertEqual(food.allergens, 'Allergens6')
        self.assertEqual(food.image, None)
        self.assertEqual(food.orderedCount, 6)
        self.assertEqual(food.ratesSum, 6)
        self.assertEqual(food.ratesCounter, 6)


    def test_FoodModel_object_creation_orderedCount_default(self):
        food = self.food7_no_orderedCount
        self.assertEqual(food.name, 'Name7')
        self.assertEqual(food.details, 'Details7')
        self.assertEqual(food.price, 7)
        self.assertEqual(food.allergens, 'Allergens7')
        self.assertIsNotNone(food.image)
        self.assertEqual(food.orderedCount, 0)
        self.assertEqual(food.ratesSum, 7)
        self.assertEqual(food.ratesCounter, 7)


    def test_FoodModel_object_creation_ratesSum_default(self):
        food = self.food8_no_ratesSum
        self.assertEqual(food.name, 'Name8')
        self.assertEqual(food.price, 8)
        self.assertEqual(food.allergens, 'Allergens8')
        self.assertIsNotNone(food.image)
        self.assertEqual(food.orderedCount, 8)
        self.assertEqual(food.ratesSum, 0)
        self.assertEqual(food.ratesCounter, 8)


    def test_FoodModel_object_creation_ratesSum_default(self):
        food = self.food9_no_ratesCounter
        self.assertEqual(food.name, 'Name9')
        self.assertEqual(food.price, 9)
        self.assertEqual(food.allergens, 'Allergens9')
        self.assertIsNotNone(food.image)
        self.assertEqual(food.orderedCount, 9)
        self.assertEqual(food.ratesSum, 9)
        self.assertEqual(food.ratesCounter, 0)
    #endregion


    #region CustomModel_tests
    def test_CustomModel_tests_object_creation_every_attributes(self):
        customer = self.customer1_every_attributes
        self.assertEqual(customer.userid, 1)
        self.assertEqual(customer.phoneno, '1')
        self.assertEqual(customer.requestToBeDeleted, True)
        self.assertEqual(customer.givenRatesCounter, 1)
        self.assertEqual(customer.givenRatesSum, 1)


    def test_CustomModel_tests_object_creation_no_userid(self):
        customer = self.customer2_no_userid
        self.assertEqual(customer.userid, -1)
        self.assertEqual(customer.phoneno, '2')
        self.assertEqual(customer.requestToBeDeleted, True)
        self.assertEqual(customer.givenRatesCounter, 2)
        self.assertEqual(customer.givenRatesSum, 2)


    def test_CustomModel_tests_object_creation_no_phoneno(self):
        customer = self.customer3_no_phoneno
        self.assertEqual(customer.userid, 3)
        self.assertEqual(customer.phoneno, 'noPhoneno')
        self.assertEqual(customer.requestToBeDeleted, True)
        self.assertEqual(customer.givenRatesCounter, 3)
        self.assertEqual(customer.givenRatesSum, 3)

    
    def test_CustomModel_tests_object_creation_no_requestToBeDeleted(self):
        customer = self.customer4_no_requestToBeDeleted
        self.assertEqual(customer.userid, 4)
        self.assertEqual(customer.phoneno, '4')
        self.assertEqual(customer.requestToBeDeleted, False)
        self.assertEqual(customer.givenRatesCounter, 4)
        self.assertEqual(customer.givenRatesSum, 4)


    def test_CustomModel_tests_object_creation_no_givenRatesCounter(self):
        customer = self.customer5_no_givenRatesCounter
        self.assertEqual(customer.userid, 5)
        self.assertEqual(customer.phoneno, '5')
        self.assertEqual(customer.requestToBeDeleted, False)
        self.assertEqual(customer.givenRatesCounter, 0)
        self.assertEqual(customer.givenRatesSum, 5)


    def test_CustomModel_tests_object_creation_no_givenRatesSum(self):
        customer = self.customer6_no_givenRatesSum
        self.assertEqual(customer.userid, 6)
        self.assertEqual(customer.phoneno, '6')
        self.assertEqual(customer.requestToBeDeleted, False)
        self.assertEqual(customer.givenRatesCounter, 6)
        self.assertEqual(customer.givenRatesSum, 0)
    #endregion


    #region OrderModel_tests
    def test_OrderModel_tests_object_creation_ratedFoodNamesFromOrderitemsList_1_foods(self):
        order = self.order0_ratedFoodNamesFromOrderitemsList_1_foods
        self.assertEqual(order.username, 'UserName0')
        self.assertEqual(order.phoneno, '0')
        self.assertEqual(order.address, 'Address0')
        self.assertEqual(order.billingAddress, 'billingAddress0')
        self.assertEqual(order.orderitems, 'Food1 burger, price: 2500, quantity: 2;')
        self.assertEqual(order.total, 'Total0')
        self.assertEqual(order.status, 'Status0')
        self.assertEqual(order.rate, 'Rate0')
        self.assertEqual(order.ratedFoodNamesFromOrderitemsList(), ['Food1 burger'])


    def test_OrderModel_tests_object_creation_ratedFoodNamesFromOrderitemsList_2_foods(self):
        order = self.order0_ratedFoodNamesFromOrderitemsList_2_foods
        self.assertEqual(order.username, 'UserName0')
        self.assertEqual(order.phoneno, '0')
        self.assertEqual(order.address, 'Address0')
        self.assertEqual(order.billingAddress, 'billingAddress0')
        self.assertEqual(order.orderitems, 'Food1 burger, price: 2500, quantity: 2;Food2 pizza, price: 1500, quantity: 1;')
        self.assertEqual(order.total, 'Total0')
        self.assertEqual(order.status, 'Status0')
        self.assertEqual(order.rate, 'Rate0')
        self.assertEqual(order.ratedFoodNamesFromOrderitemsList(), ['Food1 burger','Food2 pizza'])


    def test_OrderModel_tests_object_creation_ratedFoodNamesFromOrderitemsList_3_foods(self):
        order = self.order0_ratedFoodNamesFromOrderitemsList_3_foods
        self.assertEqual(order.username, 'UserName0')
        self.assertEqual(order.phoneno, '0')
        self.assertEqual(order.address, 'Address0')
        self.assertEqual(order.billingAddress, 'billingAddress0')
        self.assertEqual(order.orderitems, 'Food1 burger, price: 2500, quantity: 2;Food2 pizza, price: 1500, quantity: 1;Food3 pizza burger, price: 5000, quantity: 1;')
        self.assertEqual(order.total, 'Total0')
        self.assertEqual(order.status, 'Status0')
        self.assertEqual(order.rate, 'Rate0')
        self.assertEqual(order.ratedFoodNamesFromOrderitemsList(), ['Food1 burger','Food2 pizza','Food3 pizza burger'])


    def test_OrderModel_tests_object_creation_every_attributes(self):
        order = self.order1_every_attributes
        self.assertEqual(order.username, 'UserName1')
        self.assertEqual(order.phoneno, '1')
        self.assertEqual(order.address, 'Address1')
        self.assertEqual(order.billingAddress, 'billingAddress1')
        self.assertEqual(order.orderitems, 'OrderItems1')
        self.assertEqual(order.total, 'Total1')
        self.assertEqual(order.status, 'Status1')
        self.assertEqual(order.rate, 'Rate1')


    def test_OrderModel_tests_object_creation_no_username(self):
        order = self.order2_no_username
        self.assertEqual(order.username, 'noUser')
        self.assertEqual(order.phoneno, '2')
        self.assertEqual(order.address, 'Address2')
        self.assertEqual(order.billingAddress, 'billingAddress2')
        self.assertEqual(order.orderitems, 'OrderItems2')
        self.assertEqual(order.total, 'Total2')
        self.assertEqual(order.status, 'Status2')
        self.assertEqual(order.rate, 'Rate2')


    def test_OrderModel_tests_object_creation_no_phoneno(self):
        order = self.order3_no_phoneno
        self.assertEqual(order.username, 'UserName3')
        self.assertEqual(order.phoneno, 'noPhoneno')
        self.assertEqual(order.address, 'Address3')
        self.assertEqual(order.billingAddress, 'billingAddress3')
        self.assertEqual(order.orderitems, 'OrderItems3')
        self.assertEqual(order.total, 'Total3')
        self.assertEqual(order.status, 'Status3')
        self.assertEqual(order.rate, 'Rate3')


    def test_OrderModel_tests_object_creation_no_address(self):
        order = self.order4_no_address
        self.assertEqual(order.username, 'UserName4')
        self.assertEqual(order.phoneno, '4')
        self.assertEqual(order.address, 'noAddress')
        self.assertEqual(order.billingAddress, 'billingAddress4')
        self.assertEqual(order.orderitems, 'OrderItems4')
        self.assertEqual(order.total, 'Total4')
        self.assertEqual(order.status, 'Status4')
        self.assertEqual(order.rate, 'Rate4')


    def test_OrderModel_tests_object_creation_no_orderitems(self):
        order = self.order5_no_orderitems
        self.assertEqual(order.username, 'UserName5')
        self.assertEqual(order.phoneno, '5')
        self.assertEqual(order.address, 'Address5')
        self.assertEqual(order.billingAddress, 'billingAddress5')
        self.assertEqual(order.orderitems, 'noOrderitems')
        self.assertEqual(order.total, 'Total5')
        self.assertEqual(order.status, 'Status5')
        self.assertEqual(order.rate, 'Rate5')


    def test_OrderModel_tests_object_creation_no_total(self):
        order = self.order6_no_total
        self.assertEqual(order.username, 'UserName6')
        self.assertEqual(order.phoneno, '6')
        self.assertEqual(order.address, 'Address6')
        self.assertEqual(order.billingAddress, 'billingAddress6')
        self.assertEqual(order.orderitems, 'OrderItems6')
        self.assertEqual(order.total, '0')
        self.assertEqual(order.status, 'Status6')
        self.assertEqual(order.rate, 'Rate6')


    def test_OrderModel_tests_object_creation_no_status(self):
        order = self.order7_no_status
        self.assertEqual(order.username, 'UserName7')
        self.assertEqual(order.phoneno, '7')
        self.assertEqual(order.address, 'Address7')
        self.assertEqual(order.billingAddress, 'billingAddress7')
        self.assertEqual(order.orderitems, 'OrderItems7')
        self.assertEqual(order.total, 'Total7')
        self.assertEqual(order.status, 'pend')
        self.assertEqual(order.rate, 'Rate7')


    def test_OrderModel_tests_object_creation_no_rate(self):
        order = self.order8_no_rate
        self.assertEqual(order.username, 'UserName8')
        self.assertEqual(order.phoneno, '8')
        self.assertEqual(order.address, 'Address8')
        self.assertEqual(order.billingAddress, 'billingAddress8')
        self.assertEqual(order.orderitems, 'OrderItems8')
        self.assertEqual(order.total, 'Total8')
        self.assertEqual(order.status, 'Status8')
        self.assertEqual(order.rate, 'notRated')


    def test_OrderModel_tests_object_creation_no_billingAddress(self):
        order = self.order9_no_billingAddress
        self.assertEqual(order.username, 'UserName9')
        self.assertEqual(order.phoneno, '9')
        self.assertEqual(order.address, 'Address9')
        self.assertEqual(order.billingAddress, 'noBillingAddress')
        self.assertEqual(order.orderitems, 'OrderItems9')
        self.assertEqual(order.total, 'Total9')
        self.assertEqual(order.status, 'Status9')
        self.assertEqual(order.rate, 'Rate9')
    #endregion


    #region Logger_tests
    def test_Logger_tests_object_creation_every_attributes(self):
        logger = self.logger1_every_attributes
        self.assertEqual(logger.user, 'user1')
        self.assertEqual(logger.datetime, 'datetime1')
        self.assertEqual(logger.ipaddress, 'ipaddress1')
        self.assertEqual(logger.requestMethod, 'requestMethod1')
        self.assertEqual(logger.viewFunctionCalled, 'viewFunctionCalled1')
        self.assertEqual(logger.priorityInt, 1)
        self.assertEqual(logger.priorityString, 'priorityString1')
        self.assertEqual(logger.message, 'message1')


    def test_Logger_tests_object_creation_no_user(self):
        logger = self.logger2_no_user
        self.assertEqual(logger.user, 'NoUser')
        self.assertEqual(logger.datetime, 'datetime2')
        self.assertEqual(logger.ipaddress, 'ipaddress2')
        self.assertEqual(logger.requestMethod, 'requestMethod2')
        self.assertEqual(logger.viewFunctionCalled, 'viewFunctionCalled2')
        self.assertEqual(logger.priorityInt, 2)
        self.assertEqual(logger.priorityString, 'priorityString2')
        self.assertEqual(logger.message, 'message2')


    def test_Logger_tests_object_creation_no_datetime(self):
        logger = self.logger3_no_datetime
        self.assertEqual(logger.user, 'user3')
        self.assertEqual(logger.datetime, 'NoDate')
        self.assertEqual(logger.ipaddress, 'ipaddress3')
        self.assertEqual(logger.requestMethod, 'requestMethod3')
        self.assertEqual(logger.viewFunctionCalled, 'viewFunctionCalled3')
        self.assertEqual(logger.priorityInt, 3)
        self.assertEqual(logger.priorityString, 'priorityString3')
        self.assertEqual(logger.message, 'message3')


    def test_Logger_tests_object_creation_no_ipaddress(self):
        logger = self.logger4_no_ipaddress
        self.assertEqual(logger.user, 'user4')
        self.assertEqual(logger.datetime, 'datetime4')
        self.assertEqual(logger.ipaddress, 'NoIpAddress')
        self.assertEqual(logger.requestMethod, 'requestMethod4')
        self.assertEqual(logger.viewFunctionCalled, 'viewFunctionCalled4')
        self.assertEqual(logger.priorityInt, 4)
        self.assertEqual(logger.priorityString, 'priorityString4')
        self.assertEqual(logger.message, 'message4')


    def test_Logger_tests_object_creation_no_requestMethod(self):
        logger = self.logger5_no_requestMethod
        self.assertEqual(logger.user, 'user5')
        self.assertEqual(logger.datetime, 'datetime5')
        self.assertEqual(logger.ipaddress, 'ipaddress5')
        self.assertEqual(logger.requestMethod, 'NoMethod')
        self.assertEqual(logger.viewFunctionCalled, 'viewFunctionCalled5')
        self.assertEqual(logger.priorityInt, 5)
        self.assertEqual(logger.priorityString, 'priorityString5')
        self.assertEqual(logger.message, 'message5')


    def test_Logger_tests_object_creation_every_attributes(self):
        logger = self.logger6_no_viewFunctionCalled
        self.assertEqual(logger.user, 'user6')
        self.assertEqual(logger.datetime, 'datetime6')
        self.assertEqual(logger.ipaddress, 'ipaddress6')
        self.assertEqual(logger.requestMethod, 'requestMethod6')
        self.assertEqual(logger.viewFunctionCalled, 'NoFunction')
        self.assertEqual(logger.priorityInt, 6)
        self.assertEqual(logger.priorityString, 'priorityString6')
        self.assertEqual(logger.message, 'message6')


    def test_Logger_tests_object_creation_no_priorityInt(self):
        logger = self.logger7_no_priorityInt
        self.assertEqual(logger.user, 'user7')
        self.assertEqual(logger.datetime, 'datetime7')
        self.assertEqual(logger.ipaddress, 'ipaddress7')
        self.assertEqual(logger.requestMethod, 'requestMethod7')
        self.assertEqual(logger.viewFunctionCalled, 'viewFunctionCalled7')
        self.assertEqual(logger.priorityInt, 0)
        self.assertEqual(logger.priorityString, 'priorityString7')
        self.assertEqual(logger.message, 'message7')


    def test_Logger_tests_object_creation_no_priorityString(self):
        logger = self.logger8_no_priorityString
        self.assertEqual(logger.user, 'user8')
        self.assertEqual(logger.datetime, 'datetime8')
        self.assertEqual(logger.ipaddress, 'ipaddress8')
        self.assertEqual(logger.requestMethod, 'requestMethod8')
        self.assertEqual(logger.viewFunctionCalled, 'viewFunctionCalled8')
        self.assertEqual(logger.priorityInt, 8)
        self.assertEqual(logger.priorityString, 'NoPriority')
        self.assertEqual(logger.message, 'message8')


    def test_Logger_tests_object_creation_no_message(self):
        logger = self.logger9_no_message
        self.assertEqual(logger.user, 'user9')
        self.assertEqual(logger.datetime, 'datetime9')
        self.assertEqual(logger.ipaddress, 'ipaddress9')
        self.assertEqual(logger.requestMethod, 'requestMethod9')
        self.assertEqual(logger.viewFunctionCalled, 'viewFunctionCalled9')
        self.assertEqual(logger.priorityInt, 9)
        self.assertEqual(logger.priorityString, 'priorityString9')
        self.assertEqual(logger.message, 'NoMessage')
    #endregion