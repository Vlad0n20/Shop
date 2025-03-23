import factory
from factory.django import DjangoModelFactory
from faker import Faker

from .models import Image

fake = Faker()

class ImageFactory(DjangoModelFactory):
    image_url = factory.Faker('image_url')
    alt_text = factory.Faker('sentence', nb_words=4)
    image_type = factory.LazyFunction(lambda: fake.random_element(elements=('jpg', 'png', 'gif')))
    image_size = factory.Faker('random_int', min=1000, max=10000000)
    
    class Meta:
        model = Image 