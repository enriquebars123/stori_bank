from rest_framework.viewsets import ModelViewSet
from catalog.models import Transaction
from catalog.api.serializers import transaccionSerializers

class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = transaccionSerializers
