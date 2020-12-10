from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path


from api.router import router


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('main.urls')),
    path('', include('training.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
