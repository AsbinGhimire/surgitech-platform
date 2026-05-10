import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from products.models import Product, Category
from django.utils.text import slugify

def seed_products():
    data = [
        {
            'category': '4K Laparoscopy System',
            'name': 'Olympus Visera Elite II 4K UHD',
            'brand': 'Olympus',
            'price': 450000,
            'description': 'Advanced 4K UHD imaging system for surgical precision and clarity.',
            'specs': '4K Resolution\nBig Screen Support\nNBI Technology\nHDR Support',
            'badge': 'NEW',
            'is_featured': True
        },
        {
            'category': 'Anesthesia & Workstations',
            'name': 'Dräger Atlan A350 Workstation',
            'brand': 'Dräger',
            'price': 85000,
            'description': 'Comprehensive anesthesia workstation designed for patient safety and clinical efficiency.',
            'specs': 'Electronic gas mixer\nHigh-resolution touch screen\nIntegrated safety features',
            'badge': 'BEST',
            'is_featured': True
        },
        {
            'category': 'Defibrillator',
            'name': 'Zoll R Series Monitor Defibrillator',
            'brand': 'ZOLL',
            'price': 12000,
            'description': 'Professional defibrillator with See-Thru CPR and Real CPR Help technology.',
            'specs': 'Biphasic technology\nWi-Fi enabled\nOne-Step electrodes',
            'badge': 'HOT',
            'is_featured': True
        },
        {
            'category': 'Dialysis Unit',
            'name': 'Fresenius 5008S Hemodialysis System',
            'brand': 'Fresenius Medical Care',
            'price': 25000,
            'description': 'Advanced hemodialysis system offering High-Volume HDF as standard.',
            'specs': 'AutoSub Plus\nVenous Pressure Monitoring\nBlood Volume Monitor',
            'badge': 'RELIABLE',
            'is_featured': True
        },
        {
            'category': 'Electro Surgical',
            'name': 'Medtronic Valleylab FT10 Energy Platform',
            'brand': 'Medtronic',
            'price': 18000,
            'description': 'The next generation of energy, supporting all your electrosurgical needs.',
            'specs': 'Tissue Sensing Technology\nBipolar & Monopolar modes\nLigaSure support',
            'badge': 'TOP RATED',
            'is_featured': True
        },
        {
            'category': 'CT/MRI',
            'name': 'Siemens Somatom Go.Top CT Scanner',
            'brand': 'Siemens Healthineers',
            'price': 750000,
            'description': 'Advanced CT scanner designed for high performance and low dose imaging.',
            'specs': '128-slice imaging\nIterative reconstruction\nMobile workflow',
            'badge': 'PREMIUM',
            'is_featured': False
        }
    ]

    print(f"Seeding {len(data)} products...")
    for item in data:
        try:
            cat = Category.objects.get(name=item['category'])
            product, created = Product.objects.get_or_create(
                name=item['name'],
                defaults={
                    'category': cat,
                    'brand': item['brand'],
                    'price': item['price'],
                    'description': item['description'],
                    'specifications': item['specs'],
                    'badge': item['badge'],
                    'is_featured': item['is_featured'],
                    'bg_color': '#f8fafc'
                }
            )
            if created:
                print(f"Created: {product.name}")
            else:
                print(f"Skipped (exists): {product.name}")
        except Category.DoesNotExist:
            print(f"Category NOT FOUND: {item['category']}")

if __name__ == '__main__':
    seed_products()
    print("Done!")
