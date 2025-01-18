from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.shop, name='shop'),
    path('category/<int:category_id>/<int:tablecloth_id>/', views.shop_detail, name='shop_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)