from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
import calendar

from .models import Subscription,SubscriptionMeal

class SubscriptionSerializer(ModelSerializer):

    class Meta:
        model = Subscription
        fields = [
            'id',
            'customer',
            'start_date',
            'end_date',
            'created_at',
            'subscription_month'
        ]
        read_only_fields = ['id','customer','end_date','created_at']

    def validate(self, attrs):
        start_date = attrs['start_date']
        customer = self.context['customer']
        subscription_month = start_date.replace(day=1)

        if Subscription.objects.filter(
            customer=customer,
            subscription_month=subscription_month
        ).exists():
            raise serializers.ValidationError(
                "Customer already has a subscription for this month." 
            )
        
        last_day = calendar.monthrange(start_date.year,start_date.month)[1]
        end_date = start_date.replace(day=last_day)
        attrs['subscription_month'] =subscription_month
        attrs['end_date'] = end_date

        return attrs
       
        
    def create(self, validated_data):
        validated_data['customer'] = self.context['customer']

        return super().create(validated_data)



class SubscriptionMealCreateSerializer(ModelSerializer):

    class Meta:
        model = SubscriptionMeal
        fields = '__all__'


class SubscriptionMealListSerializer(ModelSerializer):

    class Meta:
        model = SubscriptionMeal
        fields = '__all__'