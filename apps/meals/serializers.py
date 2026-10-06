from rest_framework.serializers import ModelSerializer

from .models import Meal

class MealCreateSerializer(ModelSerializer):

    class Meta:
        model = Meal
        fields = '__all__'

class MealListSerializer(ModelSerializer):

    class Meta:
        model = Meal
        fields = '__all__'