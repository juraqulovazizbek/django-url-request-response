from django.urls import path

from .views import get_product_by_uuid_view


urlpatterns = [
    path('<uuid:id>', get_product_by_uuid_view),
]
