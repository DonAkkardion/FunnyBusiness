from django.test import RequestFactory, TestCase
from unittest.mock import patch
from django.core.exceptions import ObjectDoesNotExist
from .views import acceptRequest, viewProduct
from .models import Products, Review, Category, Raiting
from customers.models import CustomUser
from io import BytesIO
from .forms import ProductForm
from .views import addProduct
from django.shortcuts import reverse
from django.contrib.messages.storage.fallback import FallbackStorage

class ViewProductTest(TestCase):
    def setUp(self):
        
        self.factory = RequestFactory()
        self.category = Category.objects.create(name='Test Category')       
        self.user = CustomUser.objects.create(username='testuser', password='12345')
        self.raiting = Raiting.objects.create(name ='Raiting')
        self.product = Products.objects.create(owner=self.user.id, name='Test product', price=99, category=self.category)
        self.review = Review.objects.create(comments = 'Test review', product_raiting = self.raiting,  autor_raiting =self.raiting, target =self.user.id)
    

    def test_view_product(self):
        request = self.factory.get('/product/{}'.format(self.product.pk))

        request.user = self.user

        response = viewProduct(request, product_id=self.product.pk)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test product')
        self.assertContains(response, 'testuser')
        self.assertContains(response, 'Test review')

    def test_view_product_not_exists(self):
        with self.assertRaises(ObjectDoesNotExist):
            request = self.factory.get('/product/999')
            request.user = self.user
            response = viewProduct(request, product_id=999)

class AddProductTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = CustomUser.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Test Category')

    @patch('main.views.hashlib.sha256')
    @patch('main.views.registerProperty')
    def test_add_product(self, mock_registerProperty, mock_hashlib):

        file_data = BytesIO(b'some file data')
        file_data.name = 'myfile.txt'
        data = {
            'product_private_key': 'some private key', 
            'name': 'Test product', 
            'description': 'Test description', 
            'price': 99, 
            'isAvailable': True, 
            'category': self.category.id, 
            'img': file_data, 
            'fileEntity': file_data
        }
        form = ProductForm(data, {'img': file_data, 'fileEntity': file_data})


        self.assertFalse(form.is_valid())

        request = self.factory.post('/addProduct/', data)
        request.FILES['img'] = file_data
        request.FILES['fileEntity'] = file_data
        request.user = self.user

        mock_hashlib.return_value.digest.return_value = b'some hash'
        mock_registerProperty.return_value = {'isSuccess': True}

        response = addProduct(request)

        self.assertEqual(response.status_code, 200)


        self.assertEqual(Products.objects.count(), 0)
        product = Products.objects.first()

class AcceptRequestTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.category = Category.objects.create(name='Test Category')       
        self.user1 = CustomUser.objects.create(username='testuser1')
        self.user1.set_password('12345')
        self.user1.save()
        self.user2 = CustomUser.objects.create(username='testuser2')
        self.user2.set_password('22345')
        self.user2.save()
        self.raiting = Raiting.objects.create(name ='Raiting')
        self.product = Products.objects.create(owner=self.user1.id, futureOwner=self.user2.id, name='Test product', price=99, category=self.category, requested=True)
        self.review = Review.objects.create(comments = 'Test review', product_raiting = self.raiting,  autor_raiting =self.raiting, target =self.user1.id)
    
    def _create_request(self, private_key):
        """
        Creates a request object and attaches a dummy messages attribute
        """
        request = self.factory.post(reverse('AcceptRequest', args=[self.product.pk]), data={'private_key': private_key})
        # Attach a messages attribute to the request
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        return request
    

    @patch('main.views.is_valid_rsa_key', return_value=True)
    @patch('main.views.transferProperty', return_value={'isSuccess': False, 'error': 'Some error'})
    def test_accept_request_failure(self, mock_transferProperty, mock_is_valid_rsa_key):
        private_key = 'test_private_key'
        login = self.client.login(username='testuser1', password='12345')
        self.assertTrue(login)  # make sure you've logged in successfully
        response = self.client.post(reverse('AcceptRequest', args=[self.product.pk]), data={'private_key': private_key})



        self.assertEqual(response.status_code, 302) # expecting a redirect
        self.assertRedirects(response, reverse('ProfilePage'))
        self.assertTrue(mock_is_valid_rsa_key.called)
        self.assertTrue(mock_transferProperty.called)

        # reload the product from the database
        self.product.refresh_from_db()

        # Check that the owner has not been changed
        self.assertEqual(self.product.owner, self.user1.id)
        self.assertEqual(self.product.futureOwner, self.user2.id)
        self.assertTrue(self.product.requested)