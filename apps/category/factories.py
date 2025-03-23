import factory
from factory.django import DjangoModelFactory

from .models import Category
from apps.image.factories import ImageFactory

class CategoryFactory(DjangoModelFactory):
    name = factory.Faker('word')
    description = factory.Faker('paragraph')
    # We'll set the image to None by default and allow tests to set it if needed
    image = None
    
    class Meta:
        model = Category
        
    @factory.post_generation
    def with_image(self, create, extracted, **kwargs):
        if extracted:
            self.image = ImageFactory() 