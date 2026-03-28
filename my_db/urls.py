
from django.contrib import admin
from django.urls import path
from myapp.views import homepage,detail
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name='home'),
    path('product/<int:id>/',detail,name='podrobnee')
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
