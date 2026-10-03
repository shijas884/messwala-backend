from rest_framework.serializers import ModelSerializer

from .models import Mess

class MessSerializer(ModelSerializer):

    class Meta:
        model = Mess
        fields = [
            'id',
            'name',
            'address',
            'contact_number',
            'owner'
        ]
        read_only_fields=['id','owner']

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)