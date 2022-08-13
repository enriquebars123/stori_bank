from rest_framework import routers

from django.urls import re_path as url

from catalog.api.views import TransactionViewSet

router = routers.DefaultRouter()
router.register(r'^api/v1/transaction', TransactionViewSet)

urlpatterns = router.urls