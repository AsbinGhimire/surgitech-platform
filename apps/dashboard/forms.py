from django import forms
from products.models import Category, Product, ProductImage


ICON_CHOICES = [
    ('fa-solid fa-bed', 'Hospital Beds'),
    ('fa-solid fa-stethoscope', 'Diagnostic Equipment'),
    ('fa-solid fa-heartbeat', 'Cardiac / ICU'),
    ('fa-solid fa-lung', 'Respiratory'),
    ('fa-solid fa-syringe', 'Injection / IV'),
    ('fa-solid fa-microscope', 'Lab Equipment'),
    ('fa-solid fa-x-ray', 'Imaging'),
    ('fa-solid fa-wheelchair', 'Mobility Aids'),
    ('fa-solid fa-tooth', 'Dental'),
    ('fa-solid fa-eye', 'Ophthalmology'),
    ('fa-solid fa-baby', 'Pediatrics / Neonatal'),
    ('fa-solid fa-dna', 'Genetics / Pathology'),
    ('fa-solid fa-capsules', 'Pharmacy'),
    ('fa-solid fa-fire-extinguisher', 'Emergency / Trauma'),
    ('fa-solid fa-hospital', 'General Hospital'),
    ('fa-solid fa-box', 'Other'),
]


class CategoryForm(forms.ModelForm):
    icon = forms.ChoiceField(
        choices=ICON_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=False,
    )

    class Meta:
        model = Category
        fields = ['name', 'icon']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. Hospital Beds',
            }),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'category', 'name', 'brand', 'description', 'specifications',
            'main_image', 'price', 'old_price', 'discount_percent',
            'badge', 'bg_color', 'rating', 'review_count', 'is_featured',
        ]
        widgets = {
            'category':       forms.Select(attrs={'class': 'form-select'}),
            'name':           forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Product name'}),
            'brand':          forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. CONTEC'}),
            'description':    forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4, 'placeholder': 'Short product description…'}),
            'specifications': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 5, 'placeholder': 'Technical specs (one per line)…'}),
            'main_image':     forms.FileInput(attrs={'class': 'form-file'}),
            'price':          forms.NumberInput(attrs={'class': 'form-input', 'placeholder': '0.00'}),
            'old_price':      forms.NumberInput(attrs={'class': 'form-input', 'placeholder': '0.00'}),
            'discount_percent': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Auto-calculated if blank'}),
            'badge':          forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. New, Best Seller'}),
            'bg_color':       forms.TextInput(attrs={'class': 'form-input', 'type': 'color'}),
            'rating':         forms.NumberInput(attrs={'class': 'form-input', 'step': '0.1', 'min': '0', 'max': '5'}),
            'review_count':   forms.NumberInput(attrs={'class': 'form-input', 'placeholder': '0'}),
            'is_featured':    forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }
