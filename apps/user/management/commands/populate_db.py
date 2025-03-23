import random
from django.core.management.base import BaseCommand
from django.db import transaction

from apps.user.factories import UserFactory
from apps.image.factories import ImageFactory
from apps.category.factories import CategoryFactory
from apps.product.factories import ProductFactory
from apps.order.factories import OrderFactory, OrderItemFactory
from apps.cart.factories import CartFactory


class Command(BaseCommand):
    help = 'Populates the database with sample data for testing and development'

    def add_arguments(self, parser):
        parser.add_argument(
            '--users',
            type=int,
            default=10,
            help='Number of users to create'
        )
        parser.add_argument(
            '--images',
            type=int,
            default=30,
            help='Number of images to create'
        )
        parser.add_argument(
            '--categories',
            type=int, 
            default=8,
            help='Number of categories to create'
        )
        parser.add_argument(
            '--products',
            type=int,
            default=50,
            help='Number of products to create'
        )
        parser.add_argument(
            '--orders',
            type=int,
            default=20,
            help='Number of orders to create'
        )
        parser.add_argument(
            '--carts',
            type=int,
            default=15,
            help='Number of carts to create'
        )

    def handle(self, *args, **options):
        num_users = options['users']
        num_images = options['images']
        num_categories = options['categories']
        num_products = options['products']
        num_orders = options['orders']
        num_carts = options['carts']
        
        self.stdout.write(self.style.SUCCESS(f'Starting database population...'))
        
        with transaction.atomic():
            # Create users
            self.stdout.write(f'Creating {num_users} users...')
            users = UserFactory.create_batch(num_users)
            admin_user = UserFactory(
                email='admin@example.com',
                first_name='Admin',
                last_name='User',
                is_staff=True,
                is_superuser=True
            )
            admin_user.set_password('admin')
            admin_user.save()
            users.append(admin_user)
            
            # Create images
            self.stdout.write(f'Creating {num_images} images...')
            images = ImageFactory.create_batch(num_images)
            
            # Create categories (some with images)
            self.stdout.write(f'Creating {num_categories} categories...')
            categories = []
            for _ in range(num_categories):
                # Randomly assign an image to some categories
                with_image = random.choice([True, False])
                if with_image:
                    category = CategoryFactory(image=random.choice(images))
                else:
                    category = CategoryFactory()
                categories.append(category)
            
            # Create products (assign to categories, and add images)
            self.stdout.write(f'Creating {num_products} products...')
            products = []
            for _ in range(num_products):
                product = ProductFactory(category=random.choice(categories))
                # Add random number of images to each product
                num_product_images = random.randint(1, 5)
                product_images = random.sample(images, min(num_product_images, len(images)))
                for image in product_images:
                    product.images.add(image)
                products.append(product)
            
            # Create orders and order items
            self.stdout.write(f'Creating {num_orders} orders...')
            orders = []
            for _ in range(num_orders):
                # Create order with a random user
                order = OrderFactory(customer=random.choice(users))
                
                # Add random number of order items to the order
                num_items = random.randint(1, 6)
                for _ in range(num_items):
                    product = random.choice(products)
                    OrderItemFactory(
                        order=order,
                        product=product,
                        price=product.price,
                        quantity=random.randint(1, 5)
                    )
                
                # Recalculate order totals
                items = order.items.all()
                order.total_price = sum(item.price * item.quantity for item in items)
                order.total_discount = sum(item.discount for item in items)
                order.save()
                
                orders.append(order)
            
            # Create carts for some users
            self.stdout.write(f'Creating {num_carts} carts...')
            for _ in range(num_carts):
                user = random.choice(users)
                # Create cart with 1-4 items
                num_cart_items = random.randint(1, 4)
                
                # Use the CartFactory method that properly creates cart items
                CartFactory.create_with_products(
                    num_products=num_cart_items, 
                    customer=user
                )
        
        self.stdout.write(self.style.SUCCESS('Database successfully populated with sample data!'))
        self.stdout.write(f'''
Summary:
- {num_users} users created (including 1 admin: admin@example.com / admin)
- {num_images} images created
- {num_categories} categories created
- {num_products} products created
- {num_orders} orders created
- {num_carts} carts created
        ''') 