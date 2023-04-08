
from django.contrib import admin
from django.urls import path, include

from App_Shop import urls as app_shop_urls
from App_Login import urls as app_login
from App_Order import urls as app_order_urls
from App_Payment import urls as app_payment_urls

#to show media files
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(app_shop_urls, namespace='App_Shop')),
    path('account/', include(app_login, namespace='App_Login')),
    path('shop/', include(app_order_urls, namespace='App_Order')),
    path('payment/', include(app_payment_urls, namespace='app_payment'))
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)