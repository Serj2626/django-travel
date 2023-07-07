from django.contrib import admin
from django.urls import path, include
from travel import views
from django.conf import settings
from django.conf.urls.static import static
from routes import views as routes_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cities/', include('cities.urls')),
    path('trains/', include('trains.urls')),
    path('', routes_view.home, name='home'),
    path('about/', views.about, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
