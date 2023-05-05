from rest_framework import serializers

from mainapp.models import(
    Product, Cart, CartProduct,
)

class CartSerializer(serializers.ModelSerializer):
    products = serializers.ListField(write_only=True)
    class Meta:
        model = Cart
        fields = (
            'id', 'email', 'products', 
        )

    def create(self, validated_data):
        print(validated_data)
        email = validated_data.get('email')
        products = validated_data.get('products')
        print(email)
        print(products)
        cart = Cart.objects.create(
            email=email
        )
        for p in products:
            product = Product.objects.filter(id=p.get('product_id')).first()
            CartProduct.objects.create(
                cart=cart,
                product=product,
                amount=p.get('product_amount')
            )
        
        
        
        
        
        return cart
    
    def to_representation(self, instance):
        cart_products = instance.cart_products.all()
        result = [instance.email]
        for cp in cart_products:
            product = {
                'product_id': cp.product.id,
                'product_name': cp.product.name,
                'amount': cp.amount
            }
            result.append(product)
        return result
{"email": "gwgerh54whg@mail.ru",
                "products":[
                {
                        "product_id": 1,
                        "product_amount": 5
                    },
                    {
                        "product_id": 2,
                        "product_amount": 3
                    },
                    {
                        "product_id": 3,
                        "product_amount": 2
                    }
                ]
}