from rest_framework import serializers
from django.contrib.auth.models import User

from  .models import Order, OrderItem, MenuItem, Category, Cart

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'featured', 'category', 'category_id']

class OrderItemSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer()
    class Meta:
        model = OrderItem
        fields = ["menu_item", "quantity", "unit_price", "price"]

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(source="orderitem_set", many=True, read_only=True)
    user = UserSerializer(read_only=True)
    delivery_crew = UserSerializer(read_only=True)
    delivery_crew_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(groups__name="Delivery Crew"), source='delivery_crew', write_only=True, allow_null=True
    )
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'date', 'delivery_crew', 'delivery_crew_id', 'status', 'total', 'order_items']
        read_only_fields = ("date", "total")


class CartSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    menu_item = MenuItemSerializer(read_only=True)
    menu_item_id = serializers.PrimaryKeyRelatedField(queryset=MenuItem.objects.all(), source='menu_item', write_only=True)

    class Meta:
        model = Cart
        fields = ["user", "menu_item", "menu_item_id", "quantity", "unit_price", "price"]
        extra_kwargs = {
            "unit_price": {"read_only": True},
            "price": {"read_only": True},
        }

    def create(self, validated_data):
        validated_data["unit_price"] = validated_data.get("menu_item").price
        validated_data["price"] = validated_data["unit_price"] * validated_data["quantity"]

        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        validated_data["unit_price"] = instance.menu_item.price
        validated_data["price"] = validated_data["unit_price"] * validated_data["quantity"]

        return super().update(instance, validated_data)