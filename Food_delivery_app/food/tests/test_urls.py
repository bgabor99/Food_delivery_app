from django.test import SimpleTestCase
from django.urls import reverse, resolve
from foodapp.views import adminloginview, authenticateadmin, adminhomepageview, logoutadmin
from foodapp.views import addfood, deletefood, homepageview, signupuser, userloginview
from foodapp.views import userauthenticate, userlogout, placeorder
from foodapp.views import userorders, adminorders, acceptorder, declineorder, deliveredorder, rateaction
from foodapp.views import usermanage, deleteuser, deleteorder, adminlogs, deletelog, deletealloflogs
from foodapp.views import userprofile, deleteuserrequest, usersignuppage, contactandsupportpage
from foodapp.views import cartepage, modifyfood, zerofoodordercounters, zerofoodratecounters


class TestUrls(SimpleTestCase):


    def test_adminloginpage_url_is_resolves(self):
        url = reverse('adminloginpage')
        #print(resolve(url))
        self.assertEqual(resolve(url).func, adminloginview)


    def test_adminauthenticate_url_is_resolves(self):
        url = reverse('adminauthenticate')
        self.assertEqual(resolve(url).func, authenticateadmin)


    def test_adminhomepage_url_is_resolves(self):
        url = reverse('adminhomepage')
        self.assertEqual(resolve(url).func, adminhomepageview)

    
    def test_adminlogout_url_is_resolves(self):
        url = reverse('adminlogout')
        self.assertEqual(resolve(url).func, logoutadmin)


    def test_addfood_url_is_resolves(self):
        url = reverse('addfood')
        self.assertEqual(resolve(url).func, addfood)


    def test_deletefood_url_is_resolves_with_1(self):
        url = reverse('deletefood', args=[1])
        self.assertEqual(resolve(url).func, deletefood)


    def test_deletefood_url_is_resolves_with_50(self):
        url = reverse('deletefood', args=[50])
        self.assertEqual(resolve(url).func, deletefood)


    def test_deletefood_url_is_resolves_with_100(self):
        url = reverse('deletefood', args=[100])
        self.assertEqual(resolve(url).func, deletefood)


    def test_homepage_url_is_resolves(self):
        url = reverse('homepage')
        self.assertEqual(resolve(url).func, homepageview)


    def test_signupuser_url_is_resolves(self):
        url = reverse('signupuser')
        self.assertEqual(resolve(url).func, signupuser)


    def test_userloginpage_url_is_resolves(self):
        url = reverse('userloginpage')
        self.assertEqual(resolve(url).func, userloginview)

    
    def test_userauthenticate_url_is_resolves(self):
        url = reverse('userauthenticate')
        self.assertEqual(resolve(url).func, userauthenticate)

    
    def test_userlogout_url_is_resolves(self):
        url = reverse('userlogout')
        self.assertEqual(resolve(url).func, userlogout)


    def test_placeorder_url_is_resolves(self):
        url = reverse('placeorder')
        self.assertEqual(resolve(url).func, placeorder)


    def test_userorders_url_is_resolves(self):
        url = reverse('userorders')
        self.assertEqual(resolve(url).func, userorders)

    
    def test_adminorders_url_is_resolves(self):
        url = reverse('adminorders')
        self.assertEqual(resolve(url).func, adminorders)


    def test_userorders_url_is_resolves(self):
        url = reverse('userorders')
        self.assertEqual(resolve(url).func, userorders)


    def test_acceptorder_url_is_resolves_1(self):
        url = reverse('acceptorder', args=[1])
        self.assertEqual(resolve(url).func, acceptorder)

    
    def test_acceptorder_url_is_resolves_50(self):
        url = reverse('acceptorder', args=[50])
        self.assertEqual(resolve(url).func, acceptorder)

    
    def test_acceptorder_url_is_resolves_100(self):
        url = reverse('acceptorder', args=[100])
        self.assertEqual(resolve(url).func, acceptorder)


    def test_declineorder_url_is_resolves_1(self):
        url = reverse('declineorder', args=[1])
        self.assertEqual(resolve(url).func, declineorder)


    def test_declineorder_url_is_resolves_50(self):
        url = reverse('declineorder', args=[50])
        self.assertEqual(resolve(url).func, declineorder)


    def test_declineorder_url_is_resolves_100(self):
        url = reverse('declineorder', args=[100])
        self.assertEqual(resolve(url).func, declineorder)


    def test_deliveredorder_url_is_resolves_1(self):
        url = reverse('deliveredorder', args=[1])
        self.assertEqual(resolve(url).func, deliveredorder)


    def test_deliveredorder_url_is_resolves_50(self):
        url = reverse('deliveredorder', args=[50])
        self.assertEqual(resolve(url).func, deliveredorder)


    def test_deliveredorder_url_is_resolves_100(self):
        url = reverse('deliveredorder', args=[100])
        self.assertEqual(resolve(url).func, deliveredorder)


    def test_rateaction_url_is_resolves_1(self):
        url = reverse('rateaction', args=[1])
        self.assertEqual(resolve(url).func, rateaction)


    def test_rateaction_url_is_resolves_50(self):
        url = reverse('rateaction', args=[50])
        self.assertEqual(resolve(url).func, rateaction)


    def test_rateaction_url_is_resolves_100(self):
        url = reverse('rateaction', args=[100])
        self.assertEqual(resolve(url).func, rateaction)


    def test_usermanage_url_is_resolves(self):
        url = reverse('usermanage')
        self.assertEqual(resolve(url).func, usermanage)


    def test_deleteuser_url_is_resolves_1(self):
        url = reverse('deleteuser', args=[1, 'a'])
        self.assertEqual(resolve(url).func, deleteuser)


    def test_deleteuser_url_is_resolves_50(self):
        url = reverse('deleteuser', args=[50, 'b'])
        self.assertEqual(resolve(url).func, deleteuser)


    def test_deleteuser_url_is_resolves_100(self):
        url = reverse('deleteuser', args=[100, 'c'])
        self.assertEqual(resolve(url).func, deleteuser)


    def test_deleteorder_url_is_resolves_1(self):
        url = reverse('deleteorder', args=[1])
        self.assertEqual(resolve(url).func, deleteorder)


    def test_deleteorder_url_is_resolves_50(self):
        url = reverse('deleteorder', args=[50])
        self.assertEqual(resolve(url).func, deleteorder)


    def test_deleteorder_url_is_resolves_100(self):
        url = reverse('deleteorder', args=[100])
        self.assertEqual(resolve(url).func, deleteorder)


    def test_adminlogs_url_is_resolves(self):
        url = reverse('adminlogs')
        self.assertEqual(resolve(url).func, adminlogs)


    def test_deletelog_url_is_resolves_1(self):
        url = reverse('deletelog', args=[1])
        self.assertEqual(resolve(url).func, deletelog)


    def test_deletelog_url_is_resolves_50(self):
        url = reverse('deletelog', args=[50])
        self.assertEqual(resolve(url).func, deletelog)


    def test_deletelog_url_is_resolves_100(self):
        url = reverse('deletelog', args=[100])
        self.assertEqual(resolve(url).func, deletelog)


    def test_deletealloflogs_url_is_resolves(self):
        url = reverse('deletealloflogs')
        self.assertEqual(resolve(url).func, deletealloflogs)

    
    def test_userprofile_url_is_resolves(self):
        url = reverse('userprofile')
        self.assertEqual(resolve(url).func, userprofile)

    
    def test_deletealloflogs_url_is_resolves(self):
        url = reverse('deletealloflogs')
        self.assertEqual(resolve(url).func, deletealloflogs)


    def test_deleteuserrequest_url_is_resolves_1(self):
        url = reverse('deleteuserrequest', args=[1])
        self.assertEqual(resolve(url).func, deleteuserrequest)

    
    def test_deleteuserrequest_url_is_resolves_50(self):
        url = reverse('deleteuserrequest', args=[50])
        self.assertEqual(resolve(url).func, deleteuserrequest)

    
    def test_deleteuserrequest_url_is_resolves_100(self):
        url = reverse('deleteuserrequest', args=[100])
        self.assertEqual(resolve(url).func, deleteuserrequest)


    def test_usersignuppage_url_is_resolves(self):
        url = reverse('usersignuppage')
        self.assertEqual(resolve(url).func, usersignuppage)


    def test_supportpage_url_is_resolves(self):
        url = reverse('supportpage')
        self.assertEqual(resolve(url).func, contactandsupportpage)

    
    def test_contactpage_url_is_resolves(self):
        url = reverse('contactpage')
        self.assertEqual(resolve(url).func, contactandsupportpage)

    
    def test_cartepagee_url_is_resolves(self):
        url = reverse('carte')
        self.assertEqual(resolve(url).func, cartepage)


    def test_modifyfood_url_is_resolves(self):
        url = reverse('modifyfood')
        self.assertEqual(resolve(url).func, modifyfood)


    def test_zerofoodordercounters_url_is_resolves(self):
        url = reverse('zerofoodordercounters')
        self.assertEqual(resolve(url).func, zerofoodordercounters)

    
    def test_zerofoodratecounters_url_is_resolves(self):
        url = reverse('zerofoodratecounters')
        self.assertEqual(resolve(url).func, zerofoodratecounters)
