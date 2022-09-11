from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    catalog_data = CatalogItem.objects.all()
    return render(
        request, 
        'katalog.html',
        {
            'name' : 'Angga',
            'student_id' : '2106650065',
            'catalogs' : catalog_data,
        },
    )
