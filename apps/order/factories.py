import factory
from factory.django import DjangoModelFactory
from decimal import Decimal
import random

from .models import Order, OrderItem
from apps.user.factories import UserFactory
from apps.product.factories import ProductFactory

class OrderFactory(DjangoModelFactory):
    customer = factory.SubFactory(UserFactory)
    status = factory.LazyFunction(lambda: random.choice([choice[0] for choice in Order.OrderStatus.choices]))
    total_price = factory.LazyFunction(lambda: Decimal(str(round(random.uniform(10, 1000), 2))))
    total_discount = factory.LazyFunction(lambda: Decimal(str(round(random.uniform(0, 100), 2))))
    
    class Meta:
        model = Order

class OrderItemFactory(DjangoModelFactory):
    order = factory.SubFactory(OrderFactory)
    product = factory.SubFactory(ProductFactory)
    quantity = factory.Faker('random_int', min=1, max=10)
    price = factory.LazyFunction(lambda: Decimal(str(round(random.uniform(5, 500), 2))))
    discount = factory.LazyFunction(lambda: Decimal(str(round(random.uniform(0, 50), 2))))
    
    class Meta:
        model = OrderItem
        
    @factory.post_generation
    def recalculate_order_totals(self, create, extracted, **kwargs):
        if create and self.order:
            # Recalculate the order totals based on its items
            items = self.order.items.all()
            total_price = sum(item.price * item.quantity for item in items)
            total_discount = sum(item.discount for item in items)
            
            # Only update if there are actual changes to prevent unnecessary saves
            if self.order.total_price != total_price or self.order.total_discount != total_discount:
                self.order.total_price = total_price
                self.order.total_discount = total_discount
                self.order.save() 