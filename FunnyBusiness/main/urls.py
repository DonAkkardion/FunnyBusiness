from django.urls import path
from . import views
from Services import newFunction


urlpatterns = [
    path('', views.index, name='Hub'),
    path('addProduct', views.addProduct, name='AddProduct'),
    path('about-fb', views.about, name='About'),
    path('viewProduct/<product_id>', views.viewProduct, name='ViewProduct'),
    path('editProduct/<product_id>', views.editProduct, name='EditProduct'),
    path('deleteProduct/<product_id>', views.deleteProduct, name='DeleteProduct'),
    path('buyProduct/<product_id>', views.buyProduct, name='BuyProduct'),
    path('downloadFile/<product_id>',views.downloadFile, name='DownloadFile'),
    path('rateProduct/<product_id>',views.rateProduct, name='RateProduct'),
    path('searchProduct', views.searchProduct, name='SearchProduct'),
    path('newTest', newFunction.newFunc, name='NewTest')
]