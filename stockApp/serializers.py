from rest_framework import serializers
from .models import Category, Brand, Product, Firm, Purchase, Sale

class CategorySerializer(serializers.ModelSerializer):
    total_products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_total_products(self, obj):
        return obj.product_set.count()

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        read_only_fields = ('id',)

    def create(self, validated_data):
        return Brand.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = '__all__'
        read_only_fields = ('id',)

    def create(self, validated_data):
        return Firm.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()
    stock = serializers.ReadOnlyField()  # stock alanını read_only yapmak için

    class Meta:
        model = Product
        fields = '__all__'

    def update_stock(self, instance, validated_data):
        # Satın alma işlemi yapıldığında stock artar
        if 'purchase_set' in validated_data:
            purchases_data = validated_data.pop('purchase_set')
            total_purchase_quantity = sum(item['quantity'] for item in purchases_data)
            instance.stock += total_purchase_quantity

        # Satış işlemi yapıldığında stock azalır
        if 'sale_set' in validated_data:
            sales_data = validated_data.pop('sale_set')
            total_sale_quantity = sum(item['quantity'] for item in sales_data)
            instance.stock -= total_sale_quantity

        instance.save()
        return instance

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'
        read_only_fields = ('id', 'price_total')

    def create(self, validated_data):
        return Purchase.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'
        read_only_fields = ('id', 'price_total')

    def create(self, validated_data):
        return Sale.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance