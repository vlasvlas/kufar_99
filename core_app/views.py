#from django.db.models import Count
from django.shortcuts import render
from django.core.paginator import Paginator
#from django.db.models import F

from .models import Notebook


def notebook_list(request):
    notebooks = Notebook.objects.all().select_related().prefetch_related('image')
    paginator = Paginator(notebooks, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'title': 'Ноутбуки'
    }
    return render(request, 'core_app/notebook_list.html', context=context)


def notebook_detail(request, pk):
    data = Notebook.objects.prefetch_related('image').get(pk=pk)

    return render(request, 'core_app/notebook_detail.html', {'notebook': data})
