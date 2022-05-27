from django.contrib import admin
from django.urls import path, include
from first import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index_page),
    path('weights/', views.weights_page),
    path('weights/reboot/', views.reboot_weights_page),
    path('reboot/', views.reboot_status_page),
    path('admin/', admin.site.urls),
    path('income/', views.income_page),
    path('income/reboot/', views.reboot_income_page),
    path('task', views.task),
]

#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
