from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class FoodCategory(models.Model):
    name = models.CharField(max_length=300)
    is_publish = models.BooleanField()

    def __str__(self):
        return self.name


class Food(models.Model):
    category_id = models.ForeignKey(FoodCategory, on_delete= models.CASCADE)
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.IntegerField()
    is_special = models.BooleanField()
    is_vegan = models.BooleanField()
    is_publish =models.BooleanField()
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return self.name