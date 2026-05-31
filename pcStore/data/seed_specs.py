# seed_specs.py
import os, django, random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pcStore.settings')
django.setup()

from catalog.models import Product

# Пример: добавляем спецификации для видеокарт
for product in Product.objects.filter(categories__slug='gpu'):
    product.specifications = {
        'vram': random.choice(['4GB', '6GB', '8GB', '12GB', '16GB']),
        'gpu_brand': random.choice(['NVIDIA', 'AMD']),
        'interface': random.choice(['PCIe 3.0', 'PCIe 4.0']),
        'tdp': random.choice([150, 200, 250, 300, 350]),
    }
    product.save()
    print(f"✅ {product.title}")