
from rest_framework import serializers

class uploadTransactionSerializer(serializers.Serializer):
    account_number =  serializers.CharField()
    attachment = serializers.FileField()