from rest_framework import serializers
from catalog.models import Transaction


class transaccionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            "__all__"
        )
