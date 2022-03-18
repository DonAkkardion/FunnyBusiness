from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('customers/', include('django.contrib.auth.urls')),
    path('customers/', include('customers.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Configure Admin Titles

admin.site.site_header = 'FunnyBusiness Administration Page'
admin.site.site_title = 'Admin Tab'