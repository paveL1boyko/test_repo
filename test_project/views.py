from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from .models import FormData


def get_form_data(request):
    if request.method == 'POST':
        FormData(data=get_data_from_request(request)).save()
    return render(request, 'test_project/index.html')


def load_data(request):
    all_items = FormData.objects.all()
    return render(request, 'test_project/load.html', {'items': all_items})


def delete_item(request, pk):
    item = get_object_or_404(FormData, pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('test_project:load_data'))


def edit_items(request, pk):
    item = get_object_or_404(FormData, pk=pk)
    context = {'items': item.data, 'pk': pk}
    if request.method == 'POST':
        item.data = get_data_from_request(request)
        item.save()
        return HttpResponseRedirect(reverse('test_project:load_data'))
    return render(request, 'test_project/edit.html', context)


def get_data_from_request(request):
    return {k: v.strip() for k, v in request.POST.items() if k not in 'csrfmiddlewaretoken'}
