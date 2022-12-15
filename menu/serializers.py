from rest_framework import serializers
from .models import Food, FoodCategory, Topping


class ToppingSerializer(serializers.RelatedField):

    def to_representation(self, value):
        return value.name


class FoodSerializer(serializers.ModelSerializer):
    toppings = ToppingSerializer(many=True, read_only=True)
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'is_special', 'is_vegan', 'toppings')
        model = Food
        depth = 2


class FoodCategorySerializer(serializers.ModelSerializer):
    food = serializers.SerializerMethodField()

    class Meta:
        fields = ('id','name','food')
        model = FoodCategory

    def get_food(self, obj):
        food_options =  Food.objects.filter(category_id=obj.id, is_publish=True)
        return FoodSerializer(food_options, many=True).data


