from rest_framework.generics import ListCreateAPIView
# Create your views here.

from .models import Meal
from .serializers import(
    MealCreateSerializer,
    MealListSerializer,
)

class MealListCreateView(ListCreateAPIView):

    def get_serializer_class(self):
        if self.request.method == "POST":
            return MealCreateSerializer
        return MealListSerializer
     
    queryset =  Meal.objects.all()   
          
