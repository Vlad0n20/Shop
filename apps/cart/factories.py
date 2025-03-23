import factory
from factory.django import DjangoModelFactory

from .models import Cart
from apps.user.factories import UserFactory
from apps.order.factories import OrderItemFactory, OrderFactory
from apps.product.factories import ProductFactory

class CartFactory(DjangoModelFactory):
    customer = factory.SubFactory(UserFactory)
    
    class Meta:
        model = Cart
        
    @factory.post_generation
    def products(self, create, extracted, **kwargs):
        if not create or not extracted:
            # Simple build, or nothing to add, do nothing
            return
            
        # Add the products
        for product in extracted:
            self.products.add(product)
            
    @classmethod
    def create_with_products(cls, num_products=3, **kwargs):
        """Create a cart with a specified number of products."""
        cart = cls.create(**kwargs)
        # Create a dummy order that will be used for linking order items
        dummy_order = OrderFactory(customer=cart.customer)
        
        # Create order items linked to the dummy order
        for _ in range(num_products):
            product = ProductFactory()
            order_item = OrderItemFactory(
                order=dummy_order,
                product=product
            )
            cart.products.add(order_item)
        
        return cart 