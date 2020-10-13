from django.contrib import admin
from django.urls import include, path

from api.router import router


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
