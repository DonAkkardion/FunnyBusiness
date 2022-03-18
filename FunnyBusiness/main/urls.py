from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='Hub'),
    path('addProduct', views.addProduct, name='AddProduct'),
    path('about-fb', views.about, name='About'),
    path('viewProduct/<product_id>', views.viewProduct, name='ViewProduct'),
    path('editProduct/<product_id>', views.editProduct, name='EditProduct'),
    path('deleteProduct/<product_id>', views.deleteProduct, name='DeleteProduct'),
]