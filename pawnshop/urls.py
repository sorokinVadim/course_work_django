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
    path('new_item/<int:item_pk>', get_consignment, name="get_consignment"),
    path('api/', include(router.urls)),
    re_path(r'^item/(?P<pk>\d+)$', ItemDetailView.as_view(), name="item"),
    path('item/edit/<int:pk>', edit_item, name="item-edit"),
    re_path(r'^client/(?P<pk>\d+)$', ClientDetailView.as_view(), name="client"),
    path('client/edit/<int:pk>', edit_client, name="client-edit"),
    path('search', search, name="search"),
    path('make_fake', make_fake, name="make_fake")
]
