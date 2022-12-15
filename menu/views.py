from rest_framework.response import Response
from rest_framework import generics
from .models import FoodCategory, Food
from .serializers import FoodCategorySerializer

class HomeTextAndTitle(generics.GenericAPIView):
    queryset = Food.objects.all()

    def get(self, request):
        food_categories = FoodCategory.objects.filter(is_publish=True)

        context = {
            "request": request,
        }
        food_category_serializer = FoodCategorySerializer(food_categories,many=True, context=context)

        return Response(food_category_serializer.data)