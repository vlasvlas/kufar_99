from django.shortcuts import render
from .models import Notebook


def notebook_list(request):
    notebooks = Notebook.objects.all()
    context = {
        'notebooks': notebooks,
        'title': 'Ноутбуки'
    }
    return render(request, 'core_app/notebook_list.html', context=context)


