from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.start),
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('private/', include('privatechat.urls')),
    path('account/', include('accounts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)