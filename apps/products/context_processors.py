from .models import Category

def categories_processor(request):
    """
    Makes all categories available in all templates.
    """
    return {
        'global_categories': Category.objects.filter(parent=None).prefetch_related('children')
    }
