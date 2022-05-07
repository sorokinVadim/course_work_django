from django.urls import path, re_path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r"clients", ClientViewSet)
router.register(r"items", ItemViewSet)

urlpatterns = [
    path('', home, name="home"),
    path('offline/', offline, name="offline"),
    path('new_item', new_item, name="new_item"),
    path('api/', include(router.urls)),
    re_path(r'^item/(?P<pk>\d+)$', ItemDetailView.as_view(), name="item"),
    re_path(r'^client/(?P<pk>\d+)$', ClientDetailView.as_view(), name="client")

]
