from .models import Category

def categories_processor(request):
    """
    Makes all categories available in all templates.
    """
    return {
        'global_categories': Category.objects.all()
    }
