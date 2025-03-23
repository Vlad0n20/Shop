import factory
from factory.django import DjangoModelFactory
from decimal import Decimal
from faker import Faker
import random

from .models import Product
from apps.category.factories import CategoryFactory

# Get a Faker instance
fake = Faker()

class ProductFactory(DjangoModelFactory):
    # Use a more realistic product name approach
    name = factory.LazyFunction(lambda: f"{fake.word().capitalize()} {fake.word().capitalize()}")
    description = factory.Faker('paragraph')
    price = factory.LazyFunction(lambda: Decimal(str(round(random.uniform(5, 1000), 2))))
    is_active = True
    category = factory.SubFactory(CategoryFactory)
    
    class Meta:
        model = Product
        
    @factory.post_generation
    def images(self, create, extracted, **kwargs):
        if not create or not extracted:
            # Simple build, or nothing to add, do nothing
            return
            
        # Add the images
        for image in extracted:
            self.images.add(image) 