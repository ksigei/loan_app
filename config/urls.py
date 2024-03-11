from django.contrib import admin
from django.urls import path, include
from django.conf import settings  
from django.conf.urls.static import static 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loan.urls')), 
]

# Add settings for serving static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
